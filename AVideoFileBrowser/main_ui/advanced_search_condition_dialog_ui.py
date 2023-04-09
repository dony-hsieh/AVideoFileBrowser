# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'advanced_search_condition_dialog.main_ui'
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
        Dialog.setMinimumSize(QSize(960, 540))
        Dialog.setMaximumSize(QSize(960, 540))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.actorGroupBox = QGroupBox(Dialog)
        self.actorGroupBox.setObjectName(u"actorGroupBox")
        self.horizontalLayout = QHBoxLayout(self.actorGroupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.actorGroupBox)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.actorListWidget = QListWidget(self.actorGroupBox)
        self.actorListWidget.setObjectName(u"actorListWidget")

        self.verticalLayout_5.addWidget(self.actorListWidget)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.selectActorBtn = QPushButton(self.actorGroupBox)
        self.selectActorBtn.setObjectName(u"selectActorBtn")

        self.verticalLayout_3.addWidget(self.selectActorBtn)

        self.deselectActorBtn = QPushButton(self.actorGroupBox)
        self.deselectActorBtn.setObjectName(u"deselectActorBtn")

        self.verticalLayout_3.addWidget(self.deselectActorBtn)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.actorGroupBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_6.addWidget(self.label_2)

        self.selActorListWidget = QListWidget(self.actorGroupBox)
        self.selActorListWidget.setObjectName(u"selActorListWidget")
        self.selActorListWidget.setAutoFillBackground(False)

        self.verticalLayout_6.addWidget(self.selActorListWidget)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 3)

        self.verticalLayout_2.addWidget(self.actorGroupBox)

        self.tagGroupBox = QGroupBox(Dialog)
        self.tagGroupBox.setObjectName(u"tagGroupBox")
        self.horizontalLayout_3 = QHBoxLayout(self.tagGroupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.tagGroupBox)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_7.addWidget(self.label_3)

        self.tagListWidget = QListWidget(self.tagGroupBox)
        self.tagListWidget.setObjectName(u"tagListWidget")

        self.verticalLayout_7.addWidget(self.tagListWidget)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.selectTagBtn = QPushButton(self.tagGroupBox)
        self.selectTagBtn.setObjectName(u"selectTagBtn")

        self.verticalLayout_4.addWidget(self.selectTagBtn)

        self.deselectTagBtn = QPushButton(self.tagGroupBox)
        self.deselectTagBtn.setObjectName(u"deselectTagBtn")

        self.verticalLayout_4.addWidget(self.deselectTagBtn)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.tagGroupBox)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_8.addWidget(self.label_4)

        self.selTagListWidget = QListWidget(self.tagGroupBox)
        self.selTagListWidget.setObjectName(u"selTagListWidget")

        self.verticalLayout_8.addWidget(self.selTagListWidget)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 3)

        self.verticalLayout_2.addWidget(self.tagGroupBox)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.andRadioBtn = QRadioButton(Dialog)
        self.andRadioBtn.setObjectName(u"andRadioBtn")

        self.horizontalLayout_4.addWidget(self.andRadioBtn)

        self.orRadioBtn = QRadioButton(Dialog)
        self.orRadioBtn.setObjectName(u"orRadioBtn")

        self.horizontalLayout_4.addWidget(self.orRadioBtn)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)

        self.okBtn = QPushButton(Dialog)
        self.okBtn.setObjectName(u"okBtn")

        self.horizontalLayout_2.addWidget(self.okBtn)

        self.clearBtn = QPushButton(Dialog)
        self.clearBtn.setObjectName(u"clearBtn")

        self.horizontalLayout_2.addWidget(self.clearBtn)

        self.horizontalLayout_2.setStretch(0, 6)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 3)
        self.horizontalLayout_2.setStretch(3, 3)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.actorGroupBox.setTitle(QCoreApplication.translate("Dialog", u"Filter Actor", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"All Actors :", None))
        self.selectActorBtn.setText(QCoreApplication.translate("Dialog", u">>>", None))
        self.deselectActorBtn.setText(QCoreApplication.translate("Dialog", u"<<<", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Selected Actors :", None))
        self.tagGroupBox.setTitle(QCoreApplication.translate("Dialog", u"Filter Tag", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"All Tags :", None))
        self.selectTagBtn.setText(QCoreApplication.translate("Dialog", u">>>", None))
        self.deselectTagBtn.setText(QCoreApplication.translate("Dialog", u"<<<", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Selected Tags :", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Search Mode:", None))
        self.andRadioBtn.setText(QCoreApplication.translate("Dialog", u"AND", None))
        self.orRadioBtn.setText(QCoreApplication.translate("Dialog", u"OR", None))
        self.okBtn.setText(QCoreApplication.translate("Dialog", u"Ok", None))
        self.clearBtn.setText(QCoreApplication.translate("Dialog", u"Clear", None))
    # retranslateUi
