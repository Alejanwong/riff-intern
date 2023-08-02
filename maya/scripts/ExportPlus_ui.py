# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exportplus_1nTIQoh.ui'
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
        MainWindow.resize(508, 308)
        MainWindow.setStyleSheet(u"QRadioButton {\n"
"   \n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_2.addWidget(self.comboBox_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.radioButton = QRadioButton(self.groupBox_2)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_3.addWidget(self.radioButton)

        self.radioButton_3 = QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_3.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.groupBox_2)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.verticalLayout_3.addWidget(self.radioButton_4)

        self.radioButton_5 = QRadioButton(self.groupBox_2)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.verticalLayout_3.addWidget(self.radioButton_5)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_2.addWidget(self.checkBox)

        self.listWidget = QListWidget(self.groupBox)
        self.listWidget.setObjectName(u"listView")

        self.verticalLayout_2.addWidget(self.listWidget)


        self.horizontalLayout.addWidget(self.groupBox)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_4.addWidget(self.pushButton_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ExportPlus", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Project", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Export to", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Export List", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Export ABC -  Model", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Export shade -  Lookdev", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Export sene -  Rig", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"Export Anim ABC - Animation", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Export Preset", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"All preset", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Export", None))
    # retranslateUi

