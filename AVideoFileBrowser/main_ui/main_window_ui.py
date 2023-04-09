# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 540)
        MainWindow.setMinimumSize(QSize(640, 360))
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionRefresh = QAction(MainWindow)
        self.actionRefresh.setObjectName(u"actionRefresh")
        self.actionAddVideo = QAction(MainWindow)
        self.actionAddVideo.setObjectName(u"actionAddVideo")
        self.actionOpenInExplorer = QAction(MainWindow)
        self.actionOpenInExplorer.setObjectName(u"actionOpenInExplorer")
        self.actionDeleteVideo = QAction(MainWindow)
        self.actionDeleteVideo.setObjectName(u"actionDeleteVideo")
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.videoTab = QWidget()
        self.videoTab.setObjectName(u"videoTab")
        self.verticalLayout_5 = QVBoxLayout(self.videoTab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.searchBar = QLineEdit(self.videoTab)
        self.searchBar.setObjectName(u"searchBar")
        self.searchBar.setClearButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.searchBar)

        self.advancedConditionBtn = QPushButton(self.videoTab)
        self.advancedConditionBtn.setObjectName(u"advancedConditionBtn")

        self.horizontalLayout_2.addWidget(self.advancedConditionBtn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.searchBtn = QPushButton(self.videoTab)
        self.searchBtn.setObjectName(u"searchBtn")

        self.horizontalLayout_6.addWidget(self.searchBtn)

        self.resetBtn = QPushButton(self.videoTab)
        self.resetBtn.setObjectName(u"resetBtn")

        self.horizontalLayout_6.addWidget(self.resetBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.videoListWidget = QListWidget(self.videoTab)
        self.videoListWidget.setObjectName(u"videoListWidget")

        self.verticalLayout_3.addWidget(self.videoListWidget)

        self.verticalLayout_3.setStretch(2, 7)

        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.tabWidget.addTab(self.videoTab, "")
        self.actorTab = QWidget()
        self.actorTab.setObjectName(u"actorTab")
        self.verticalLayout_7 = QVBoxLayout(self.actorTab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.newActorBtn = QPushButton(self.actorTab)
        self.newActorBtn.setObjectName(u"newActorBtn")

        self.horizontalLayout_3.addWidget(self.newActorBtn)

        self.delActorBtn = QPushButton(self.actorTab)
        self.delActorBtn.setObjectName(u"delActorBtn")

        self.horizontalLayout_3.addWidget(self.delActorBtn)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.curSelectedActorLabel = QLabel(self.actorTab)
        self.curSelectedActorLabel.setObjectName(u"curSelectedActorLabel")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.curSelectedActorLabel.setFont(font)

        self.verticalLayout_6.addWidget(self.curSelectedActorLabel)

        self.actorListWidget = QListWidget(self.actorTab)
        self.actorListWidget.setObjectName(u"actorListWidget")

        self.verticalLayout_6.addWidget(self.actorListWidget)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.tabWidget.addTab(self.actorTab, "")
        self.tagTab = QWidget()
        self.tagTab.setObjectName(u"tagTab")
        self.verticalLayout_9 = QVBoxLayout(self.tagTab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.newTagBtn = QPushButton(self.tagTab)
        self.newTagBtn.setObjectName(u"newTagBtn")

        self.horizontalLayout_4.addWidget(self.newTagBtn)

        self.delTagBtn = QPushButton(self.tagTab)
        self.delTagBtn.setObjectName(u"delTagBtn")

        self.horizontalLayout_4.addWidget(self.delTagBtn)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.curSelectedTagLabel = QLabel(self.tagTab)
        self.curSelectedTagLabel.setObjectName(u"curSelectedTagLabel")
        self.curSelectedTagLabel.setFont(font)

        self.verticalLayout_8.addWidget(self.curSelectedTagLabel)

        self.tagListWidget = QListWidget(self.tagTab)
        self.tagListWidget.setObjectName(u"tagListWidget")

        self.verticalLayout_8.addWidget(self.tagListWidget)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.tabWidget.addTab(self.tagTab, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label_5.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.filenameViewLabel = QLabel(self.groupBox)
        self.filenameViewLabel.setObjectName(u"filenameViewLabel")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.filenameViewLabel)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.line)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.numberViewLabel = QLabel(self.groupBox)
        self.numberViewLabel.setObjectName(u"numberViewLabel")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.numberViewLabel)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label)

        self.titleViewLabel = QLabel(self.groupBox)
        self.titleViewLabel.setObjectName(u"titleViewLabel")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.titleViewLabel)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.descriptionViewLabel = QLabel(self.groupBox)
        self.descriptionViewLabel.setObjectName(u"descriptionViewLabel")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.descriptionViewLabel)

        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.line_2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_3)

        self.actorViewLabel = QLabel(self.groupBox)
        self.actorViewLabel.setObjectName(u"actorViewLabel")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.actorViewLabel)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_4)

        self.tagViewLabel = QLabel(self.groupBox)
        self.tagViewLabel.setObjectName(u"tagViewLabel")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.tagViewLabel)


        self.verticalLayout_10.addLayout(self.formLayout)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.editInfoBtn = QPushButton(self.centralwidget)
        self.editInfoBtn.setObjectName(u"editInfoBtn")

        self.horizontalLayout_5.addWidget(self.editInfoBtn)

        self.genThumbnailBtn = QPushButton(self.centralwidget)
        self.genThumbnailBtn.setObjectName(u"genThumbnailBtn")

        self.horizontalLayout_5.addWidget(self.genThumbnailBtn)

        self.playVideoBtn = QPushButton(self.centralwidget)
        self.playVideoBtn.setObjectName(u"playVideoBtn")

        self.horizontalLayout_5.addWidget(self.playVideoBtn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_2.addWidget(self.graphicsView)

        self.verticalLayout_2.setStretch(0, 6)
        self.verticalLayout_2.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 3)

        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 960, 18))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionAddVideo)
        self.menuFile.addAction(self.actionDeleteVideo)
        self.menuFile.addAction(self.actionOpenInExplorer)
        self.menuFile.addAction(self.actionRefresh)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Local AVVideo Browser", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionRefresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.actionAddVideo.setText(QCoreApplication.translate("MainWindow", u"Add Video", None))
        self.actionOpenInExplorer.setText(QCoreApplication.translate("MainWindow", u"Open In Explorer", None))
        self.actionDeleteVideo.setText(QCoreApplication.translate("MainWindow", u"Delete Video", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.advancedConditionBtn.setText(QCoreApplication.translate("MainWindow", u"Advanced Conditions", None))
        self.searchBtn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.resetBtn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.videoTab), QCoreApplication.translate("MainWindow", u"Video", None))
        self.newActorBtn.setText(QCoreApplication.translate("MainWindow", u"New Actor", None))
        self.delActorBtn.setText(QCoreApplication.translate("MainWindow", u"Delete Selected Actor", None))
        self.curSelectedActorLabel.setText(QCoreApplication.translate("MainWindow", u"Current selected actor : ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.actorTab), QCoreApplication.translate("MainWindow", u"Actor", None))
        self.newTagBtn.setText(QCoreApplication.translate("MainWindow", u"New Tag", None))
        self.delTagBtn.setText(QCoreApplication.translate("MainWindow", u"Delete Selected Tag", None))
        self.curSelectedTagLabel.setText(QCoreApplication.translate("MainWindow", u"Current selected tag : ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tagTab), QCoreApplication.translate("MainWindow", u"Tag", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Video Info", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Filename : ", None))
        self.filenameViewLabel.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Number : ", None))
        self.numberViewLabel.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Title : ", None))
        self.titleViewLabel.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Description : ", None))
        self.descriptionViewLabel.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Actor : ", None))
        self.actorViewLabel.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tags : ", None))
        self.tagViewLabel.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.editInfoBtn.setText(QCoreApplication.translate("MainWindow", u"Edit Info", None))
        self.genThumbnailBtn.setText(QCoreApplication.translate("MainWindow", u"Generate Thumbnail", None))
        self.playVideoBtn.setText(QCoreApplication.translate("MainWindow", u"Play Video", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi
