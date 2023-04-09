import sqlite3
import pathlib
from AVideoFileBrowser.definitions import DB_FILE_PATH


class Database:
    def __init__(self):
        self.__connection = None

        if DB_FILE_PATH.exists():
            self.__connection = sqlite3.connect(DB_FILE_PATH)
            # check correct tables were existed in database
            if not self.__checkDbTables():
                self.__buildNewDB()
                self.__buildTables()
                print("[*] Database rebuilt.")
        else:
            # create new database if it's not existed
            self.__connection = sqlite3.connect(DB_FILE_PATH)
            self.__buildTables()
            print("[*] New database built.")

        self.__connection.execute("PRAGMA foreign_keys=ON;")  # sqlite must activate foreign keys manually
        print("[*] Database connected.")

    def __del__(self):
        self.__connection.close()

    def executeR(self, statement: str, args: tuple = tuple(), fetch_counts: int = 0):
        cursor = self.__connection.cursor()
        if len(args):
            cursor.execute(statement, args)
        else:
            cursor.execute(statement)
        if fetch_counts <= 0:
            return cursor.fetchall()
        if fetch_counts == 1:
            return cursor.fetchone()
        if fetch_counts > 1:
            return cursor.fetchmany(fetch_counts)

    def executeCUD(self, statement: str, args: tuple = tuple()):
        cursor = self.__connection.cursor()
        if len(args):
            cursor.execute(statement, args)
        else:
            cursor.execute(statement)
        self.__connection.commit()

    def __checkDbTables(self):
        qArgs = ["Video", "Actor", "Tag", "VideoActorRelation", "VideoTagRelation"]
        statement = f"""
            SELECT COUNT(name) FROM sqlite_master WHERE type='table' AND name IN ({','.join('?' * len(qArgs))});
        """
        cursor = self.__connection.cursor()
        cursor.execute(statement, qArgs)
        if cursor.fetchone()[0] == len(qArgs):
            return True
        return False

    def __buildNewDB(self):
        self.__connection.close()
        if DB_FILE_PATH.exists():
            pathlib.Path.unlink(DB_FILE_PATH)
        self.__connection = sqlite3.connect(DB_FILE_PATH)

    def __buildTables(self):
        script = """
            CREATE TABLE "Video" (
                "number"	          TEXT,
                "filename"	          TEXT  NOT NULL,
                "title"	              TEXT,
                "description"	      TEXT,
                "thumbnail_filename"  TEXT,
                PRIMARY KEY("filename")
            );
            
            CREATE TABLE "Actor" (
                "name"	TEXT  NOT NULL,
                PRIMARY KEY("name")
            );
            
            CREATE TABLE "Tag" (
                "name"	TEXT  NOT NULL,
                PRIMARY KEY("name")
            );
            
            CREATE TABLE "VideoActorRelation" (
                "filename"	    TEXT  NOT NULL,
                "actor_name"	TEXT  NOT NULL,
                PRIMARY KEY("filename","actor_name"),
                FOREIGN KEY("actor_name") REFERENCES "Actor"("name") 
                    ON UPDATE CASCADE   ON DELETE CASCADE,
                FOREIGN KEY("filename") REFERENCES "Video"("filename")
                    ON UPDATE CASCADE   ON DELETE CASCADE
            );
            
            CREATE TABLE "VideoTagRelation" (
                "filename"	TEXT  NOT NULL,
                "tag_name"	TEXT  NOT NULL,
                PRIMARY KEY("filename","tag_name"),
                FOREIGN KEY("filename") REFERENCES "Video"("filename")
                    ON UPDATE CASCADE   ON DELETE CASCADE,
                FOREIGN KEY("tag_name") REFERENCES "Tag"("name")
                    ON UPDATE CASCADE   ON DELETE CASCADE
            );
        """
        cursor = self.__connection.cursor()
        cursor.executescript(script)
        self.__connection.commit()


if __name__ == "__main__":
    db = Database()
