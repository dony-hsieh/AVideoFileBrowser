# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'video_player.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtMultimediaWidgets import QVideoWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(640, 480))
        MainWindow.setMaximumSize(QSize(640, 480))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.videoWidget = QVideoWidget(self.centralwidget)
        self.videoWidget.setObjectName(u"videoWidget")

        self.verticalLayout.addWidget(self.videoWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.controlButton = QPushButton(self.centralwidget)
        self.controlButton.setObjectName(u"controlButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.controlButton.sizePolicy().hasHeightForWidth())
        self.controlButton.setSizePolicy(sizePolicy1)
        self.controlButton.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.controlButton)

        self.labelCurTime = QLabel(self.centralwidget)
        self.labelCurTime.setObjectName(u"labelCurTime")

        self.horizontalLayout.addWidget(self.labelCurTime)

        self.timeSlider = QSlider(self.centralwidget)
        self.timeSlider.setObjectName(u"timeSlider")
        self.timeSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.timeSlider)

        self.labelDurTime = QLabel(self.centralwidget)
        self.labelDurTime.setObjectName(u"labelDurTime")

        self.horizontalLayout.addWidget(self.labelDurTime)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 18))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Video Player", None))
        self.controlButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.labelCurTime.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.labelDurTime.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
    # retranslateUi
