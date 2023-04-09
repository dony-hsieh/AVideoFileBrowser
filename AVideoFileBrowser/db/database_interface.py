import pathlib
import shutil
import json
from PySide2.QtCore import QThread
from typing import Callable

from AVideoFileBrowser.db import database
from AVideoFileBrowser.definitions import VIDEO_DIR_PATH, THUMBNAIL_DIR_PATH
from AVideoFileBrowser.thumbnail_generator import thumbnail_generator


class TaskThread(QThread):
    def __init__(self, task: Callable):
        super(TaskThread, self).__init__()
        self.task = task
        self.args = ()

    def run(self):
        self.task(*self.args)

    def startTask(self, args: tuple = ()):
        self.args = args if isinstance(args, tuple) else ()
        self.start()

    def connectSignal(self, started_slot: Callable = None, finished_slot: Callable = None):
        if isinstance(started_slot, Callable):
            self.started.connect(started_slot)
        if isinstance(finished_slot, Callable):
            self.finished.connect(finished_slot)


class SearchConditionWrapper:
    def __init__(self):
        self.keywords = []
        self.actors = []
        self.tags = []

    def setKeywords(self, keywords: list):
        if not keywords:
            self.keywords.clear()
            return
        self.keywords = list(set(keywords))
        self.keywords.sort()

    def setActors(self, actors: list):
        if not actors:
            self.actors.clear()
            return
        self.actors = list(set(actors))
        self.actors.sort()

    def setTags(self, tags: list):
        if not tags:
            self.tags.clear()
            return
        self.tags = list(set(tags))
        self.tags.sort()

    def resetAll(self):
        self.keywords.clear()
        self.actors.clear()
        self.tags.clear()

    def isAdvancedSearchCondSet(self) -> bool:
        return bool(self.actors or self.tags)

    def emptyCondition(self) -> bool:
        return not (self.keywords or self.actors or self.tags)


class DbInterface:
    def __init__(self):
        self.db = database.Database()
        self.checkDataPath()
        self.tnGenerator = thumbnail_generator.ThumbnailGenerator()
        self.supVideoFileTypes = [".mp4", ".mkv", ".avi"]
        self.copyFileTask = TaskThread(shutil.copy)
        self.genThumbnailTask = TaskThread(self.tnGenerator.generate)
        self.dumpJsonTask = TaskThread(self.__dumpJson)

    def checkDataPath(self):
        if not VIDEO_DIR_PATH.exists():
            VIDEO_DIR_PATH.mkdir(parents=True, exist_ok=True)
        if not THUMBNAIL_DIR_PATH.exists():
            THUMBNAIL_DIR_PATH.mkdir(parents=True, exist_ok=True)

    def listDiskThumbnails(self) -> list:
        return [
            str(p.absolute()) for p in THUMBNAIL_DIR_PATH.glob("**/*")
            if p.suffix == self.tnGenerator.THUMBNAIL_FILETYPE
        ]

    def listDiskVideos(self) -> list:
        return [str(p.absolute()) for p in VIDEO_DIR_PATH.glob("**/*") if p.suffix in self.supVideoFileTypes]

    def listDbVideos(self) -> list:
        return [tup[0] for tup in self.db.executeR("SELECT filename FROM Video;")]

    def deleteDbVideos(self, filename_list: list):
        if not filename_list:
            return
        statement = f"DELETE FROM Video WHERE filename IN ({','.join('?' * len(filename_list))})"
        self.db.executeCUD(statement, tuple(filename_list))

    def insertVideos(self, filename_list: list):
        if not filename_list:
            return
        statement = f"""
            INSERT INTO Video (number, filename, title, description, thumbnail_filename) 
                VALUES {"('',?,'','','')," * len(filename_list)}
        """
        statement = statement.strip()
        statement = statement[:len(statement)-1] + ";"  # remove the final ',' and add ';'
        self.db.executeCUD(statement, tuple(filename_list))

    def getVideoInfo(self, video_filename: str) -> tuple:
        statement = "SELECT filename, number, title, description FROM Video WHERE filename=?;"
        res = self.db.executeR(statement, (video_filename,), 1)
        return res

    def getVideoThumbnail(self, video_filename: str) -> str:
        statement = "SELECT thumbnail_filename FROM Video WHERE filename=?;"
        res = self.db.executeR(statement, (video_filename,), 1)
        if res is not None:
            return str(res[0])
        return ""

    def listVideoActors(self, video_filename: str) -> list:
        statement = "SELECT actor_name FROM VideoActorRelation WHERE filename=?;"
        return [tup[0] for tup in self.db.executeR(statement, (video_filename,))]

    def listVideoTags(self, video_filename: str):
        statement = "SELECT tag_name FROM VideoTagRelation WHERE filename=?;"
        return [tup[0] for tup in self.db.executeR(statement, (video_filename,))]

    def listVideoActorsComplement(self, video_filename: str):
        statement = """
            SELECT name FROM Actor WHERE name NOT IN (
                SELECT actor_name FROM VideoActorRelation WHERE filename=?
            );
        """
        res = self.db.executeR(statement, (video_filename,))
        if not res:
            return []
        return [tup[0] for tup in res]

    def listVideoTagComplement(self, video_filename: str):
        statement = """
            SELECT name FROM Tag WHERE name NOT IN (
                SELECT tag_name FROM VideoTagRelation WHERE filename=? 
            );
        """
        res = self.db.executeR(statement, (video_filename,))
        if not res:
            return []
        return [tup[0] for tup in res]

    def findActorExisted(self, name: str) -> bool:
        if name:
            foundName = self.db.executeR("SELECT name FROM Actor WHERE name=?;", (name,), 1)
            return False if foundName is None else True
        return False

    def findTagExisted(self, name: str) -> bool:
        if name:
            foundTag = self.db.executeR("SELECT name FROM Tag WHERE name=?;", (name,), 1)
            return False if foundTag is None else True
        return False

    def listActors(self) -> list:
        return [tup[0] for tup in self.db.executeR("SELECT name FROM Actor;")]

    def listTags(self) -> list:
        return [tup[0] for tup in self.db.executeR("SELECT name FROM Tag;")]

    def insertActor(self, name: str):
        if name:
            self.db.executeCUD("INSERT INTO Actor(name) VALUES (?);", (name,))

    def insertTag(self, name: str):
        if name:
            self.db.executeCUD("INSERT INTO Tag(name) VALUES (?);", (name,))

    def deleteActor(self, name: str):
        if name:
            self.db.executeCUD("DELETE FROM Actor WHERE name=?;", (name,))

    def deleteTag(self, name: str):
        if name:
            self.db.executeCUD("DELETE FROM Tag WHERE name=?;", (name,))

    def autoUpdateDbVideos(self):
        diskFiles = set(self.listDiskVideos())
        dbFiles = set(self.listDbVideos())
        inte = diskFiles & dbFiles  # intersection set
        removeFromDb = list(dbFiles - inte)
        insertToDb = list(diskFiles - inte)
        self.deleteDbVideos(removeFromDb)
        self.insertVideos(insertToDb)

    def autoRemoveUnusedThumbnails(self):
        statement = "SELECT thumbnail_filename FROM Video;"
        dbThumbnails = [tup[0] for tup in self.db.executeR(statement) if len(tup[0]) > 0]
        diskThumbnails = self.listDiskThumbnails()
        for p in diskThumbnails:
            if p not in dbThumbnails:
                pathlib.Path(p).unlink(missing_ok=True)

    def findThumbnailExisted(self, video_filename: str) -> bool:
        res = self.db.executeR(
            "SELECT filename, thumbnail_filename FROM Video WHERE filename=?;", (video_filename,), 1
        )
        return res is None or (len(res[1]) > 0 and pathlib.Path(res[1]).exists())

    def generateThumbnail(self, video_filename: str):
        if self.findThumbnailExisted(video_filename):
            return
        destThumbnailPath = str(
            THUMBNAIL_DIR_PATH.joinpath(pathlib.Path(video_filename).stem)
        ) + self.tnGenerator.THUMBNAIL_FILETYPE
        self.genThumbnailTask.startTask((video_filename, destThumbnailPath))
        self.db.executeCUD(
            "UPDATE Video SET thumbnail_filename=? WHERE filename=?;", (destThumbnailPath, video_filename)
        )

    def userAddVideo(self, video_filename: str):
        newFilename = VIDEO_DIR_PATH.joinpath(pathlib.Path(video_filename).name)
        if newFilename.exists():
            return
        self.copyFileTask.startTask((video_filename, newFilename))  # test
        self.autoUpdateDbVideos()

    def userDeleteVideo(self, video_filename: str):
        path = pathlib.Path(video_filename)
        if path.exists():
            path.unlink(missing_ok=True)
            self.autoUpdateDbVideos()

    def updateVideoInfo(self, video_filename: str, number: str, title: str, description: str):
        curVideoInfo = self.getVideoInfo(video_filename)
        if curVideoInfo is not None:
            # form statement
            _, curNumber, curTitle, curDescription = curVideoInfo
            updateStatementList, argList = [], []
            for attrStat, newAttr, curAttr in zip(
                    ("number", "title", "description"),
                    (number, title, description),
                    (curNumber, curTitle, curDescription)
            ):
                if newAttr != curAttr:
                    updateStatementList.append(f"{attrStat}=?")
                    argList.append(newAttr)
            if not updateStatementList:
                return
            statement = f"UPDATE Video SET {','.join(updateStatementList)} WHERE filename=?;"
            self.db.executeCUD(statement, (*argList, video_filename))

    def updateVideoActors(self, video_filename: str, inserting_actors: list, deleting_actors: list):
        delStatement = f"""
            DELETE FROM VideoActorRelation 
            WHERE filename=? AND actor_name IN ({','.join('?' * len(deleting_actors))});
        """
        insStatement = f"""
            INSERT OR REPLACE INTO VideoActorRelation(filename, actor_name) 
            VALUES {','.join(['(?, ?)'] * len(inserting_actors))};
        """
        delArgs = (video_filename, *deleting_actors)
        insArgs = []
        for actor in inserting_actors:
            insArgs += [video_filename, actor]
        insArgs = tuple(insArgs)
        if delArgs:
            self.db.executeCUD(delStatement, delArgs)
        if insArgs:
            self.db.executeCUD(insStatement, insArgs)

    def updateVideoTags(self, video_filename: str, inserting_tags: list, deleting_tags: list):
        delStatement = f"""
            DELETE FROM VideoTagRelation
            WHERE filename=? AND tag_name IN ({','.join('?' * len(deleting_tags))});
        """
        insStatement = f"""
            INSERT OR REPLACE INTO VideoTagRelation(filename, tag_name)
            VALUES {','.join(['(?, ?)'] * len(inserting_tags))};
        """
        delArgs = (video_filename, *deleting_tags)
        insArgs = []
        for tag in inserting_tags:
            insArgs += [video_filename, tag]
        insArgs = tuple(insArgs)
        if delArgs:
            self.db.executeCUD(delStatement, delArgs)
        if insArgs:
            self.db.executeCUD(insStatement, insArgs)

    def parseKeywordSearchStatement(self, keywords: list) -> tuple[str, tuple]:
        if not keywords:
            return "", ()
        kwStatementUnit = 'filename LIKE ? OR title LIKE ? OR number LIKE ? OR description LIKE ?'
        statement = f"""
            SELECT filename FROM Video WHERE {' OR '.join([kwStatementUnit] * len(keywords))}
        """.strip()
        argSet = []
        for kw in keywords:
            argSet += [f"%{kw}%"] * 4
        return statement, tuple(argSet)

    def parseAdvancedSearchStatement(
            self,
            actors: list,
            tags: list,
            use_intersection_search: bool = False
    ) -> tuple[str, tuple]:
        if not actors and not tags:
            return "", ()
        actorStatementSub = f"""
            SELECT filename FROM VideoActorRelation WHERE actor_name IN ({','.join('?' * len(actors))})
        """.strip()
        tagStatementSub = f"""
            SELECT filename FROM VideoTagRelation WHERE tag_name IN ({','.join('?' * len(tags))})
        """.strip()
        statementSet, argSet = [], []
        if actors:
            statementSet.append(actorStatementSub)
            argSet += actors
        if tags:
            statementSet.append(tagStatementSub)
            argSet += tags
        searchMode = " INTERSECT " if use_intersection_search else " UNION "
        return f"{searchMode.join(statementSet)}", tuple(argSet)

    def conditionallySearchVideos(
            self,
            search_cond: SearchConditionWrapper,
            use_intersection_search: bool = False
    ) -> list:
        if search_cond.emptyCondition():
            return []
        kwSearchStatement, kwSearchArgs = self.parseKeywordSearchStatement(search_cond.keywords)
        advSearchStatement, advSearchArgs = self.parseAdvancedSearchStatement(
            search_cond.actors, search_cond.tags, use_intersection_search
        )
        finalStatementSet, finalArgSet = [], ()
        # the search priority of advanced search is higher than keyword search
        if advSearchStatement:
            finalStatementSet.append(advSearchStatement)
            finalArgSet += advSearchArgs
        if kwSearchStatement:
            finalStatementSet.append(kwSearchStatement)
            finalArgSet += kwSearchArgs
        searchMode = " INTERSECT " if use_intersection_search else " UNION "
        finalStatement = searchMode.join(finalStatementSet) + ";"
        return [tup[0] for tup in self.db.executeR(finalStatement, finalArgSet)]

    def __dumpJson(self, obj: any, export_path: str):
        with open(pathlib.Path(export_path).absolute(), mode="w", encoding="utf-8") as writingFile:
            json.dump(obj, writingFile, ensure_ascii=False, indent=2)

    def exportJson(self, export_path: str):
        jsonObj = {
            "actors": sorted(self.listActors()),
            "tags": sorted(self.listTags()),
            "videos": []
        }
        allVideos = sorted(self.listDbVideos())
        for filename in allVideos:
            videoJsonObj = {}
            info = self.getVideoInfo(filename)  # (filename, number, title, description)
            if info is not None:
                videoJsonObj["filename"] = info[0]
                videoJsonObj["number"] = info[1]
                videoJsonObj["title"] = info[2]
                videoJsonObj["description"] = info[3]
                videoJsonObj["actor"] = sorted(self.listVideoActors(filename))
                videoJsonObj["tag"] = sorted(self.listVideoTags(filename))
                jsonObj["videos"].append(videoJsonObj)
        self.dumpJsonTask.startTask((jsonObj, export_path))


if __name__ == "__main__":
    dbInte = DbInterface()
    dbInte.autoUpdateDbVideos()
