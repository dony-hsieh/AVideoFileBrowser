from PySide2.QtWidgets import (
    QApplication, QMainWindow, QListWidgetItem, QWidget, QGraphicsScene, QGraphicsView, QMessageBox, QFileDialog,
    QShortcut
)
from PySide2.QtCore import Qt, Signal, QDir
from PySide2.QtGui import QPixmap, QWheelEvent, QKeySequence, QMovie, QCloseEvent, QShowEvent
import pathlib
import subprocess
import sys

from AVideoFileBrowser.main_ui import (
    main_window_ui, new_actor_dialog_ui, new_tag_dialog_ui, edit_video_info_dialog_ui, busy_waiting_indicator_ui,
    advanced_search_condition_dialog_ui
)
from AVideoFileBrowser.video_player import video_player
from AVideoFileBrowser.db import database_interface
from AVideoFileBrowser.definitions import RESOURCE_DIR_PATH


class NewActorDialogWindow(QWidget):
    def __init__(self):
        super(NewActorDialogWindow, self).__init__()
        self.ui = new_actor_dialog_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.lineEdit.setPlaceholderText("Add a new actor...")


class NewTagDialogWindow(QWidget):
    def __init__(self):
        super(NewTagDialogWindow, self).__init__()
        self.ui = new_tag_dialog_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.lineEdit.setPlaceholderText("Add a new tag...")


class EditVideoInfoDialogWindow(QWidget):
    def __init__(self):
        super(EditVideoInfoDialogWindow, self).__init__()
        self.ui = edit_video_info_dialog_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.filenameLabel.setWordWrap(True)
        self.ui.candActorListWidget.setSortingEnabled(True)
        self.ui.candTagListWidget.setSortingEnabled(True)
        self.ui.selActorListWidget.setSortingEnabled(True)
        self.ui.selTagListWidget.setSortingEnabled(True)


class BusyWaitingIndicatorWindow(QWidget):
    closed = Signal()

    def __init__(self):
        super(BusyWaitingIndicatorWindow, self).__init__()
        self.ui = busy_waiting_indicator_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.spinnerMovie = QMovie(str(RESOURCE_DIR_PATH.joinpath("spinner.gif")))
        self.ui.gifDisplayLabel.setMovie(self.spinnerMovie)

    def closeEvent(self, event: QCloseEvent) -> None:
        self.spinnerMovie.stop()
        self.closed.emit()

    def showEvent(self, event: QShowEvent) -> None:
        self.spinnerMovie.start()


class AdvancedSearchCondDialogWindow(QWidget):
    def __init__(self):
        super(AdvancedSearchCondDialogWindow, self).__init__()
        self.ui = advanced_search_condition_dialog_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.actorListWidget.setSortingEnabled(True)
        self.ui.tagListWidget.setSortingEnabled(True)
        self.ui.selActorListWidget.setSortingEnabled(True)
        self.ui.selTagListWidget.setSortingEnabled(True)
        self.ui.orRadioBtn.setChecked(True)


class ApplicationWindow(QMainWindow):
    def __init__(self):
        # setup mainWindow
        super(ApplicationWindow, self).__init__()
        self.ui = main_window_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        # instance and settings of widgets
        self.newActorDialog = NewActorDialogWindow()
        self.newTagDialog = NewTagDialogWindow()
        self.editVideoInfoDialog = EditVideoInfoDialogWindow()
        self.busyWaitIndicatorDialog = BusyWaitingIndicatorWindow()
        self.advancedSearchCondDialog = AdvancedSearchCondDialogWindow()
        self.videoPlayer = video_player.MainWindow()
        self.dbInterface = database_interface.DbInterface()
        self.graphicsScene = QGraphicsScene()
        self.ui.videoListWidget.setSortingEnabled(True)
        self.ui.actorListWidget.setSortingEnabled(True)
        self.ui.tagListWidget.setSortingEnabled(True)
        self.ui.graphicsView.setDragMode(QGraphicsView.ScrollHandDrag)
        self.ui.graphicsView.setScene(self.graphicsScene)
        self.ui.actionRefresh.setShortcut(QKeySequence("f5"))
        self.ui.actionExit.setShortcut(QKeySequence("alt+f4"))
        self.ui.actionOpenInExplorer.setShortcut(QKeySequence("ctrl+o"))
        self.ui.actionDeleteVideo.setShortcut(QKeySequence("del"))
        self.ui.searchBar.setPlaceholderText("Type something to search...")
        self.ui.searchBar.setClearButtonEnabled(True)
        self.searchShortcut = QShortcut(QKeySequence("return"), self)

        # connections of signals and slots
        QApplication.instance().focusChanged.connect(self.appFocusChanged)
        self.ui.playVideoBtn.clicked.connect(self.playVideo)
        self.ui.newActorBtn.clicked.connect(self.openNewActorDialog)
        self.ui.newTagBtn.clicked.connect(self.openNewTagDialog)
        self.ui.editInfoBtn.clicked.connect(self.openEditVideoInfoDialog)
        self.ui.videoListWidget.itemClicked.connect(self.getSelectedVideo)
        self.ui.delActorBtn.clicked.connect(self.delSelectedActor)
        self.ui.delTagBtn.clicked.connect(self.delSelectedTag)
        self.newActorDialog.ui.okBtn.clicked.connect(self.addNewActor)
        self.newTagDialog.ui.okBtn.clicked.connect(self.addNewTag)
        self.newActorDialog.ui.cancelBtn.clicked.connect(self.newActorDialog.close)
        self.newTagDialog.ui.cancelBtn.clicked.connect(self.newTagDialog.close)
        self.ui.actorListWidget.currentItemChanged.connect(self.getSelectedActor)
        self.ui.tagListWidget.currentItemChanged.connect(self.getSelectedTag)
        self.ui.genThumbnailBtn.clicked.connect(self.generateThumbnail)
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionRefresh.triggered.connect(self.refreshAllData)
        self.ui.actionAddVideo.triggered.connect(self.userAddVideo)
        self.ui.actionOpenInExplorer.triggered.connect(self.openVideoInExplorer)
        self.ui.actionDeleteVideo.triggered.connect(self.userDeleteVideo)
        self.ui.actionExport.triggered.connect(self.exportJson)
        self.editVideoInfoDialog.ui.discardEditBtn.clicked.connect(self.editVideoInfoDialog.close)
        self.editVideoInfoDialog.ui.saveEditBtn.clicked.connect(self.saveEditedVideoInfo)
        self.editVideoInfoDialog.ui.actorSelectBtn.clicked.connect(self.actorSelBtnClicked)
        self.editVideoInfoDialog.ui.actorDeselectBtn.clicked.connect(self.actorDeselBtnClicked)
        self.editVideoInfoDialog.ui.tagSelectBtn.clicked.connect(self.tagSelBtnClicked)
        self.editVideoInfoDialog.ui.tagDeselectBtn.clicked.connect(self.tagDeselBtnClicked)
        self.busyWaitIndicatorDialog.closed.connect(self.refreshAllData)
        self.dbInterface.copyFileTask.connectSignal(
            started_slot=self.openBusyWaitIndicatorDialog,
            finished_slot=self.busyWaitIndicatorDialog.close
        )
        self.dbInterface.genThumbnailTask.connectSignal(
            started_slot=self.openBusyWaitIndicatorDialog,
            finished_slot=self.busyWaitIndicatorDialog.close
        )
        self.dbInterface.dumpJsonTask.connectSignal(
            started_slot=self.openBusyWaitIndicatorDialog,
            finished_slot=self.busyWaitIndicatorDialog.close
        )
        self.ui.searchBtn.clicked.connect(self.executeSearch)
        self.ui.resetBtn.clicked.connect(self.resetSearchCondition)
        self.ui.advancedConditionBtn.clicked.connect(self.openAdvancedSearchCondDialog)
        self.advancedSearchCondDialog.ui.okBtn.clicked.connect(self.setAdvancedSearchCondition)
        self.advancedSearchCondDialog.ui.clearBtn.clicked.connect(self.clearAdvancedSearchCondition)
        self.advancedSearchCondDialog.ui.selectActorBtn.clicked.connect(self.selectActorToSearch)
        self.advancedSearchCondDialog.ui.selectTagBtn.clicked.connect(self.selectTagToSearch)
        self.advancedSearchCondDialog.ui.deselectActorBtn.clicked.connect(self.deselectActorFromSearch)
        self.advancedSearchCondDialog.ui.deselectTagBtn.clicked.connect(self.deselectTagFromSearch)
        self.searchShortcut.activated.connect(self.executeSearch)

        # data container
        self.videoList = []  # element = (absolute_path, filename_stem)
        self.videoDict = {}  # element = {filename_stem: absolute_path}
        self.actorList = []  # element = actor_name
        self.tagList = []  # element = tag_name
        self.selVideoCandActorList = []  # for video info editing
        self.selVideoCandTagList = []  # for video info editing
        self.selVideoActorList = []  # for video info editing
        self.selVideoTagList = []  # for video info editing
        self.curEditingVideoFilename = ""
        self.videoListWidgetCurItemText = ""
        self.searchConditionWrapper = database_interface.SearchConditionWrapper()  # for video search
        self.searchVideoResults = []  # for video search

        # initialize some logics
        self.refreshAllData()

    def refreshAllData(self):
        self.dbInterface.autoUpdateDbVideos()
        self.dbInterface.autoRemoveUnusedThumbnails()
        self.updateVideoList()
        self.updateVideoListWidget()
        self.updateActorList()
        self.updateTagList()
        self.updateActorListWidget()
        self.updateTagListWidget()
        self.ui.advancedConditionBtn.setStyleSheet("background-color: light gray")
        if self.searchConditionWrapper.isAdvancedSearchCondSet():
            self.ui.advancedConditionBtn.setStyleSheet("background-color: #abe0ab")
        print("[*] Data refreshed.")

    def playVideo(self):
        item = self.ui.videoListWidget.currentItem()
        self.videoListWidgetCurItemText = item.text() if item is not None else ""
        if self.videoListWidgetCurItemText:
            self.videoPlayer.setWindowModality(Qt.ApplicationModal)  # set focus on video player
            self.videoPlayer.loadMedia(self.videoDict[self.videoListWidgetCurItemText])

    def appFocusChanged(self, old: QWidget, now: QWidget):
        # consider the moment when the mainWindow is focused on
        if old is None and QApplication.instance().activeWindow() == self:
            # set currentItem of the videoListWidget when user return to mainWindow
            if self.videoListWidgetCurItemText and self.ui.videoListWidget.currentItem() is None:
                items = self.ui.videoListWidget.findItems(self.videoListWidgetCurItemText, Qt.MatchExactly)
                if len(items) == 1:
                    self.ui.videoListWidget.setCurrentItem(items[0])
                self.getSelectedVideo(items[0])

    def setEditInfoDialogDataView(self, filename: str):
        if filename:
            # get number, title, and description
            number, title, description = "", "", ""
            videoInfo = self.dbInterface.getVideoInfo(filename)
            if videoInfo is not None:
                _, number, title, description = videoInfo
                self.curEditingVideoFilename = filename
            # get complements of actors and tags of the video
            self.updateCandActorAndTagList(filename)
            # get actors and tags of the video
            self.updateSelVideoActorAndTagList(filename)
            # set initial data view
            self.updateCandActorAndTagListWidget()
            self.updateSelVideoActorAndTagListWidget()
            self.editVideoInfoDialog.ui.filenameLabel.setText(f"Filename:\n{filename}")
            self.editVideoInfoDialog.ui.numberLineEdit.setText(number)
            self.editVideoInfoDialog.ui.titleLineEdit.setText(title)
            self.editVideoInfoDialog.ui.descriptionTextEdit.setPlainText(description)

    def setAdvancedSearchCondDialogDataView(self):
        self.advancedSearchCondDialog.ui.actorListWidget.clear()
        self.advancedSearchCondDialog.ui.tagListWidget.clear()
        self.advancedSearchCondDialog.ui.selActorListWidget.clear()
        self.advancedSearchCondDialog.ui.selTagListWidget.clear()
        self.advancedSearchCondDialog.ui.actorListWidget.addItems(self.actorList)
        self.advancedSearchCondDialog.ui.tagListWidget.addItems(self.tagList)
        self.advancedSearchCondDialog.ui.selActorListWidget.addItems(self.searchConditionWrapper.actors)
        self.advancedSearchCondDialog.ui.selTagListWidget.addItems(self.searchConditionWrapper.tags)

    def openNewActorDialog(self):
        self.newActorDialog.setWindowModality(Qt.ApplicationModal)
        self.newActorDialog.show()
        self.newActorDialog.ui.lineEdit.clear()

    def openNewTagDialog(self):
        self.newTagDialog.setWindowModality(Qt.ApplicationModal)
        self.newTagDialog.show()
        self.newTagDialog.ui.lineEdit.clear()

    def openEditVideoInfoDialog(self):
        item = self.ui.videoListWidget.currentItem()
        self.videoListWidgetCurItemText = item.text() if item is not None else ""
        if self.videoListWidgetCurItemText:
            filename = self.videoDict[self.videoListWidgetCurItemText]
            self.refreshAllData()
            self.editVideoInfoDialog.setWindowModality(Qt.ApplicationModal)
            self.editVideoInfoDialog.show()
            self.setEditInfoDialogDataView(filename)

    def openBusyWaitIndicatorDialog(self):
        self.busyWaitIndicatorDialog.setWindowModality(Qt.ApplicationModal)
        self.busyWaitIndicatorDialog.show()

    def openAdvancedSearchCondDialog(self):
        self.refreshAllData()
        self.advancedSearchCondDialog.setWindowModality(Qt.ApplicationModal)
        self.advancedSearchCondDialog.show()
        self.setAdvancedSearchCondDialogDataView()

    def updateVideoList(self):
        videos = self.dbInterface.listDbVideos()
        self.videoList = [(p, str(pathlib.Path(p).stem)) for p in videos]
        self.videoList.sort(key=lambda x: x[1])
        self.videoDict = {k: v for v, k in self.videoList}

    def updateVideoListWidget(self):
        items = [t[1] for t in self.videoList]
        self.ui.videoListWidget.clear()
        self.ui.videoListWidget.addItems(items)

    def updateActorList(self):
        actors = self.dbInterface.listActors()
        self.actorList = sorted(actors, key=lambda x: x)

    def updateTagList(self):
        tags = self.dbInterface.listTags()
        self.tagList = sorted(tags, key=lambda x: x)

    def updateActorListWidget(self):
        self.ui.actorListWidget.clear()
        self.ui.actorListWidget.addItems(self.actorList)

    def updateTagListWidget(self):
        self.ui.tagListWidget.clear()
        self.ui.tagListWidget.addItems(self.tagList)

    def updateGraphicsViewWidget(self):
        # Reset graphicScene
        pxItems = self.graphicsScene.items()
        if pxItems:
            for pxItem in pxItems:
                self.graphicsScene.removeItem(pxItem)
        # Get thumbnail
        thumbnailFilename = self.dbInterface.getVideoThumbnail(
            self.videoDict[self.videoListWidgetCurItemText]
        )
        if thumbnailFilename and pathlib.Path(thumbnailFilename).exists():
            thumbnail = QPixmap(thumbnailFilename)
            self.graphicsScene.addPixmap(thumbnail)

    def updateCandActorAndTagList(self, filename: str = ""):
        if filename == "":
            self.selVideoCandActorList.clear()
            self.selVideoCandTagList.clear()
            return
        self.selVideoCandActorList = self.dbInterface.listVideoActorsComplement(filename)
        self.selVideoCandTagList = self.dbInterface.listVideoTagComplement(filename)
        self.selVideoCandActorList.sort()
        self.selVideoCandTagList.sort()

    def updateCandActorAndTagListWidget(self):
        self.editVideoInfoDialog.ui.candActorListWidget.clear()
        self.editVideoInfoDialog.ui.candTagListWidget.clear()
        self.editVideoInfoDialog.ui.candActorListWidget.addItems(self.selVideoCandActorList)
        self.editVideoInfoDialog.ui.candTagListWidget.addItems(self.selVideoCandTagList)

    def updateSelVideoActorAndTagList(self, filename: str = ""):
        if filename == "":
            self.selVideoActorList.clear()
            self.selVideoTagList.clear()
            return
        self.selVideoActorList = self.dbInterface.listVideoActors(filename)
        self.selVideoTagList = self.dbInterface.listVideoTags(filename)
        self.selVideoActorList.sort()
        self.selVideoTagList.sort()

    def updateSelVideoActorAndTagListWidget(self):
        self.editVideoInfoDialog.ui.selActorListWidget.clear()
        self.editVideoInfoDialog.ui.selTagListWidget.clear()
        self.editVideoInfoDialog.ui.selActorListWidget.addItems(self.selVideoActorList)
        self.editVideoInfoDialog.ui.selTagListWidget.addItems(self.selVideoTagList)

    def addNewActor(self):
        newActor = self.newActorDialog.ui.lineEdit.text().strip()
        if newActor:
            if not self.dbInterface.findActorExisted(newActor):
                self.dbInterface.insertActor(newActor)
        self.updateActorList()
        self.updateActorListWidget()
        self.newActorDialog.close()

    def addNewTag(self):
        newTag = self.newTagDialog.ui.lineEdit.text().strip()
        if newTag:
            if not self.dbInterface.findTagExisted(newTag):
                self.dbInterface.insertTag(newTag)
        self.updateTagList()
        self.updateTagListWidget()
        self.newTagDialog.close()

    def delSelectedActor(self):
        curSelActor = self.ui.actorListWidget.currentItem()
        if curSelActor is not None:
            reply = QMessageBox.question(
                self,
                "Delete Actor",
                f"Are you sure to delete actor\n\"{curSelActor.text()}\"?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            if reply == QMessageBox.Yes and self.dbInterface.findActorExisted(curSelActor.text()):
                self.dbInterface.deleteActor(curSelActor.text())
        self.updateActorList()
        self.updateActorListWidget()

    def delSelectedTag(self):
        curSelTag = self.ui.tagListWidget.currentItem()
        if curSelTag is not None:
            reply = QMessageBox.question(
                self,
                "Delete Tag",
                f"Are you sure to delete tag\n\"{curSelTag.text()}\"?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            if reply == QMessageBox.Yes and self.dbInterface.findTagExisted(curSelTag.text()):
                self.dbInterface.deleteTag(curSelTag.text())
        self.updateTagList()
        self.updateTagListWidget()

    def getSelectedVideo(self, item: QListWidgetItem):
        filename, number, title, description = "", "", "", ""
        self.videoListWidgetCurItemText = item.text() if item is not None else ""
        if self.videoListWidgetCurItemText:
            filename = self.videoDict[self.videoListWidgetCurItemText]
        videoInfo = self.dbInterface.getVideoInfo(filename)
        if videoInfo is not None:
            _, number, title, description = videoInfo
        # set video info display
        self.ui.filenameViewLabel.setText(filename)
        self.ui.numberViewLabel.setText(number)
        self.ui.titleViewLabel.setText(title)
        self.ui.descriptionViewLabel.setText(description)
        # set actors and tags display
        self.updateSelVideoActorAndTagList(filename)
        self.ui.actorViewLabel.setText(", ".join(self.selVideoActorList))
        self.ui.tagViewLabel.setText(", ".join(self.selVideoTagList))
        # set "generate thumbnail" button enable or disable
        self.ui.genThumbnailBtn.setEnabled(False)
        if not self.dbInterface.findThumbnailExisted(filename):
            self.ui.genThumbnailBtn.setEnabled(True)
        # update the display of thumbnail
        self.updateGraphicsViewWidget()

    def getSelectedActor(self, item: QListWidgetItem):
        if item is None:
            self.ui.curSelectedActorLabel.setText("Current selected actor : ")
            return
        self.ui.curSelectedActorLabel.setText(f"Current selected actor : {item.text()}")

    def getSelectedTag(self, item: QListWidgetItem):
        if item is None:
            self.ui.curSelectedTagLabel.setText("Current selected tag : ")
            return
        self.ui.curSelectedTagLabel.setText(f"Current selected tag : {item.text()}")

    def generateThumbnail(self):
        item = self.ui.videoListWidget.currentItem()
        self.videoListWidgetCurItemText = item.text() if item is not None else ""
        if self.videoListWidgetCurItemText:
            self.dbInterface.generateThumbnail(self.videoDict[self.videoListWidgetCurItemText])
            self.updateGraphicsViewWidget()
            if self.ui.genThumbnailBtn.isEnabled():
                self.ui.genThumbnailBtn.setEnabled(False)

    # Override
    def wheelEvent(self, event: QWheelEvent):
        if self.ui.graphicsView.underMouse() and event.modifiers() == Qt.ControlModifier:
            # handle zoom in and zoom out
            factor = 1.1 ** (event.delta() / 240.0)
            self.ui.graphicsView.scale(factor, factor)

    def userAddVideo(self):
        fileTypeFilter = [f"*{ft}" for ft in self.dbInterface.supVideoFileTypes]
        filename, _ = QFileDialog.getOpenFileName(dir=QDir.homePath(), filter=";;".join(fileTypeFilter))
        if filename:
            self.dbInterface.userAddVideo(filename)
        self.refreshAllData()

    def userDeleteVideo(self):
        item = self.ui.videoListWidget.currentItem()
        self.videoListWidgetCurItemText = item.text() if item is not None else ""
        if self.videoListWidgetCurItemText:
            filename = self.videoDict[self.videoListWidgetCurItemText]
            reply = QMessageBox.question(
                self,
                "Delete Video",
                f"Are you sure to delete video\n\"{self.videoListWidgetCurItemText}\"",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                self.dbInterface.userDeleteVideo(filename)
                self.refreshAllData()

    def actorSelBtnClicked(self):
        selCandActorItem = self.editVideoInfoDialog.ui.candActorListWidget.currentItem()
        if selCandActorItem is not None:
            selCandActorName = selCandActorItem.text()
            self.selVideoCandActorList.remove(selCandActorName)
            self.selVideoActorList.append(selCandActorName)
            self.selVideoActorList.sort()
            self.updateCandActorAndTagListWidget()
            self.updateSelVideoActorAndTagListWidget()

    def actorDeselBtnClicked(self):
        selActorItem = self.editVideoInfoDialog.ui.selActorListWidget.currentItem()
        if selActorItem is not None:
            selActorName = selActorItem.text()
            self.selVideoActorList.remove(selActorName)
            self.selVideoCandActorList.append(selActorName)
            self.selVideoCandActorList.sort()
            self.updateCandActorAndTagListWidget()
            self.updateSelVideoActorAndTagListWidget()

    def tagSelBtnClicked(self):
        selCandTagItem = self.editVideoInfoDialog.ui.candTagListWidget.currentItem()
        if selCandTagItem is not None:
            selCandTagName = selCandTagItem.text()
            self.selVideoCandTagList.remove(selCandTagName)
            self.selVideoTagList.append(selCandTagName)
            self.selVideoTagList.sort()
            self.updateCandActorAndTagListWidget()
            self.updateSelVideoActorAndTagListWidget()

    def tagDeselBtnClicked(self):
        selTagItem = self.editVideoInfoDialog.ui.selTagListWidget.currentItem()
        if selTagItem is not None:
            selTagName = selTagItem.text()
            self.selVideoTagList.remove(selTagName)
            self.selVideoCandTagList.append(selTagName)
            self.selVideoCandTagList.sort()
            self.updateCandActorAndTagListWidget()
            self.updateSelVideoActorAndTagListWidget()

    def saveEditedVideoInfo(self):
        self.dbInterface.updateVideoInfo(
            self.curEditingVideoFilename,
            self.editVideoInfoDialog.ui.numberLineEdit.text(),
            self.editVideoInfoDialog.ui.titleLineEdit.text(),
            self.editVideoInfoDialog.ui.descriptionTextEdit.toPlainText()
        )
        self.dbInterface.updateVideoActors(
            self.curEditingVideoFilename, self.selVideoActorList, self.selVideoCandActorList
        )
        self.dbInterface.updateVideoTags(
            self.curEditingVideoFilename, self.selVideoTagList, self.selVideoCandTagList
        )
        self.editVideoInfoDialog.close()
        self.curEditingVideoFilename = ""
        self.refreshAllData()

    def openVideoInExplorer(self):
        item = self.ui.videoListWidget.currentItem()
        self.videoListWidgetCurItemText = item.text() if item is not None else ""
        if self.videoListWidgetCurItemText:
            filename = self.videoDict[self.videoListWidgetCurItemText]
            subprocess.Popen("explorer /select, " + filename)

    def resetSearchCondition(self):
        self.advancedSearchCondDialog.ui.orRadioBtn.setChecked(True)
        self.searchConditionWrapper.resetAll()
        self.ui.searchBar.clear()
        self.searchVideoResults.clear()
        self.refreshAllData()

    def clearAdvancedSearchCondition(self):
        # triggered when user in advancedSearchCondDialog
        # only clear selActorListWidget and selTagListWidget
        self.advancedSearchCondDialog.ui.selActorListWidget.clear()
        self.advancedSearchCondDialog.ui.selTagListWidget.clear()
        self.advancedSearchCondDialog.ui.orRadioBtn.setChecked(True)

    def selectActorToSearch(self):
        item = self.advancedSearchCondDialog.ui.actorListWidget.currentItem()
        if item is not None:
            text = item.text()
            if not self.advancedSearchCondDialog.ui.selActorListWidget.findItems(text, Qt.MatchExactly):
                self.advancedSearchCondDialog.ui.selActorListWidget.addItem(text)

    def selectTagToSearch(self):
        item = self.advancedSearchCondDialog.ui.tagListWidget.currentItem()
        if item is not None:
            text = item.text()
            if not self.advancedSearchCondDialog.ui.selTagListWidget.findItems(text, Qt.MatchExactly):
                self.advancedSearchCondDialog.ui.selTagListWidget.addItem(text)

    def deselectActorFromSearch(self):
        item = self.advancedSearchCondDialog.ui.selActorListWidget.currentItem()
        if item is not None:
            self.advancedSearchCondDialog.ui.selActorListWidget.takeItem(
                self.advancedSearchCondDialog.ui.selActorListWidget.row(item)
            )

    def deselectTagFromSearch(self):
        item = self.advancedSearchCondDialog.ui.selTagListWidget.currentItem()
        if item is not None:
            self.advancedSearchCondDialog.ui.selTagListWidget.takeItem(
                self.advancedSearchCondDialog.ui.selTagListWidget.row(item)
            )

    def setAdvancedSearchCondition(self):
        selectedActors = [
            self.advancedSearchCondDialog.ui.selActorListWidget.item(i).text()
            for i in range(self.advancedSearchCondDialog.ui.selActorListWidget.count())
        ]
        selectedTags = [
            self.advancedSearchCondDialog.ui.selTagListWidget.item(i).text()
            for i in range(self.advancedSearchCondDialog.ui.selTagListWidget.count())
        ]
        self.searchConditionWrapper.setActors(selectedActors)
        self.searchConditionWrapper.setTags(selectedTags)
        self.advancedSearchCondDialog.close()
        self.refreshAllData()

    def executeSearch(self):
        text = self.ui.searchBar.text()
        keywords = [k for k in text.split(" ") if len(k) > 0]
        self.searchConditionWrapper.setKeywords(keywords)
        if self.searchConditionWrapper.emptyCondition():
            self.refreshAllData()
            return
        # store search result
        self.searchVideoResults = list(
            self.dbInterface.conditionallySearchVideos(
                self.searchConditionWrapper, self.advancedSearchCondDialog.ui.andRadioBtn.isChecked()
            )
        )
        # show search video results
        # exclude invalid results
        videoList = sorted(
            [str(pathlib.Path(p).stem) for p in self.searchVideoResults if p in self.videoDict.values()]
        )
        self.ui.videoListWidget.clear()
        self.ui.videoListWidget.addItems(videoList)

    def exportJson(self):
        filename, _ = QFileDialog.getSaveFileName(dir=QDir.homePath(), filter="Json Files (*.json)")
        if filename:
            self.dbInterface.exportJson(filename)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    applicationWindow = ApplicationWindow()
    applicationWindow.show()
    sys.exit(app.exec_())
