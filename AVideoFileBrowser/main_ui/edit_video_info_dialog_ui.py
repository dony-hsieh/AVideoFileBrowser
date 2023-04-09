# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_video_info_dialog.main_ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(960, 540)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(960, 540))
        Dialog.setMaximumSize(QSize(960, 540))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.filenameLabel = QLabel(Dialog)
        self.filenameLabel.setObjectName(u"filenameLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.filenameLabel.sizePolicy().hasHeightForWidth())
        self.filenameLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.filenameLabel)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label)

        self.numberLineEdit = QLineEdit(Dialog)
        self.numberLineEdit.setObjectName(u"numberLineEdit")
        sizePolicy1.setHeightForWidth(self.numberLineEdit.sizePolicy().hasHeightForWidth())
        self.numberLineEdit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.numberLineEdit)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 7)

        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFrameShape(QFrame.NoFrame)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.titleLineEdit = QLineEdit(Dialog)
        self.titleLineEdit.setObjectName(u"titleLineEdit")
        sizePolicy1.setHeightForWidth(self.titleLineEdit.sizePolicy().hasHeightForWidth())
        self.titleLineEdit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.titleLineEdit)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 7)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.descriptionTextEdit = QPlainTextEdit(Dialog)
        self.descriptionTextEdit.setObjectName(u"descriptionTextEdit")
        sizePolicy1.setHeightForWidth(self.descriptionTextEdit.sizePolicy().hasHeightForWidth())
        self.descriptionTextEdit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.descriptionTextEdit)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 7)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 2)
        self.verticalLayout_3.setStretch(2, 2)
        self.verticalLayout_3.setStretch(3, 2)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4)

        self.candActorListWidget = QListWidget(Dialog)
        self.candActorListWidget.setObjectName(u"candActorListWidget")

        self.verticalLayout_6.addWidget(self.candActorListWidget)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.actorSelectBtn = QPushButton(Dialog)
        self.actorSelectBtn.setObjectName(u"actorSelectBtn")

        self.verticalLayout_5.addWidget(self.actorSelectBtn)

        self.actorDeselectBtn = QPushButton(Dialog)
        self.actorDeselectBtn.setObjectName(u"actorDeselectBtn")

        self.verticalLayout_5.addWidget(self.actorDeselectBtn)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_7.addWidget(self.label_5)

        self.selActorListWidget = QListWidget(Dialog)
        self.selActorListWidget.setObjectName(u"selActorListWidget")

        self.verticalLayout_7.addWidget(self.selActorListWidget)


        self.horizontalLayout_6.addLayout(self.verticalLayout_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_8.addWidget(self.label_6)

        self.candTagListWidget = QListWidget(Dialog)
        self.candTagListWidget.setObjectName(u"candTagListWidget")

        self.verticalLayout_8.addWidget(self.candTagListWidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_8)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tagSelectBtn = QPushButton(Dialog)
        self.tagSelectBtn.setObjectName(u"tagSelectBtn")

        self.verticalLayout_4.addWidget(self.tagSelectBtn)

        self.tagDeselectBtn = QPushButton(Dialog)
        self.tagDeselectBtn.setObjectName(u"tagDeselectBtn")

        self.verticalLayout_4.addWidget(self.tagDeselectBtn)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_9.addWidget(self.label_7)

        self.selTagListWidget = QListWidget(Dialog)
        self.selTagListWidget.setObjectName(u"selTagListWidget")

        self.verticalLayout_9.addWidget(self.selTagListWidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.line_2 = QFrame(Dialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.saveEditBtn = QPushButton(Dialog)
        self.saveEditBtn.setObjectName(u"saveEditBtn")

        self.horizontalLayout_7.addWidget(self.saveEditBtn)

        self.discardEditBtn = QPushButton(Dialog)
        self.discardEditBtn.setObjectName(u"discardEditBtn")

        self.horizontalLayout_7.addWidget(self.discardEditBtn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(3, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.filenameLabel.setText(QCoreApplication.translate("Dialog", u"Filename: ", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Number: ", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Title :      ", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Description: ", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Candidate Actor :", None))
        self.actorSelectBtn.setText(QCoreApplication.translate("Dialog", u">>>", None))
        self.actorDeselectBtn.setText(QCoreApplication.translate("Dialog", u"<<<", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Selected Actor :", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Candidate Tag :", None))
        self.tagSelectBtn.setText(QCoreApplication.translate("Dialog", u">>>", None))
        self.tagDeselectBtn.setText(QCoreApplication.translate("Dialog", u"<<<", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Selected Tag :", None))
        self.saveEditBtn.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.discardEditBtn.setText(QCoreApplication.translate("Dialog", u"Discard", None))
    # retranslateUi
