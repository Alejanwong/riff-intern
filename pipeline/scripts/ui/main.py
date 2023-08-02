# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file manager_fixnScnku.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import os

__DIRNAME__ = os.path.dirname(__file__)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1054, 796)
        MainWindow.setStyleSheet(u"#centralwidget {	  \n"
"	background-color: #222133;	\n"
"}\n"
"\n"
"QTreeView {\n"
"    background-color: #10101a;\n"
"    color: rgb(240, 240, 240);\n"
"    font-size: 13px\n"
"}\n"
" \n"
"QComboBox {\n"
"    border: none;\n"
"    background-color: #10101a;\n"
"	color: rgb(240, 240, 240);\n"
"	font-size: 15px\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: #10101a;\n"
"    font-size: 14pt;\n"
"    border-radius: 16px;\n"
"    background-color: #ffffff;\n"
"    padding: 5px 30px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   \n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: #ffffff;\n"
"    font-size: 10pt\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #ffffff;\n"
"    background-color: #10101a;\n"
"}\n"
"\n"
"\n"
"QCheckBox {\n"
"  \n"
"	color: rgb(240, 240, 240);\n"
"	font-size: 12px\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: none;\n"
"	font-size: 15px\n"
"}\n"
"\n"
"QGroupBox {\n"
"     background-color: #2c2a42;\n"
"	 font-size: 13px;\n"
"	 color: #ffffff;\n"
"     border-radius: 5px;\n"
"     padding-top: 15px\n"
""
                        "}\n"
"\n"
"QTabWidget {\n"
"	font-size: 15px;  \n"
"    \n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"  \n"
"  top:-1px; \n"
"  \n"
"} \n"
"\n"
"QTabBar::tab {\n"
"  \n"
"  color: #ffffff;\n"
"  background-color: #10101a;\n"
"  border-top-left-radius: 10px;\n"
"  border-top-right-radius: 10px;\n"
"  padding: 6px;\n"
"} \n"
"\n"
"QTabBar::tab:selected { \n"
"  color: #10101a;\n"
"  background: #ffffff;\n"
"  margin-bottom: -1px; \n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: none;\n"
"    background-color: #222133;	\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border-radius: 5px;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QListWidget {\n"
"    border: none;\n"
"    background-color: #10101a;    	\n"
"	color: rgb(240, 240, 240);\n"
"    font-size: 13px;\n"
"    padding: 10px\n"
"\n"
"}\n"
"\n"
"#tab_2 {\n"
"     background-color: #2c2a42;\n"
"     \n"
"}\n"
"\n"
"#tab_3 {\n"
"     background-color: #2c2a42;\n"
"}\n"
"\n"
"QFrame {\n"
"    border: none;\n"
"}\n"
"\n"
"#frame {\n"
"     background-color: #10101a;\n"
"     border-radius: 14px; \n"
"}\n"
"\n"
"#frame_2 {\n"
"     background-color: #ffffff;\n"
"     border-radius: 14px; \n"
"}\n"
"\n"
"#frame_3 {\n"
"     background-color: #10101a;\n"
""
                        "     border-radius: 14px; \n"
"}\n"
"\n"
"#frame_4 {\n"
"     background-color: #ffffff;\n"
"     border-radius: 14px; \n"
"}\n"
"\n"
"#frame_5 {\n"
"     background-color: #10101a;\n"
"     border-radius: 16px; \n"
"}\n"
"\n"
"#frame_6 {\n"
"     background-color: #2c2a42;\n"
"     border-radius: 16px; \n"
"\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"{}/place.png".format(__DIRNAME__)))

        self.verticalLayout_4.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 0, -1)
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 6, -1, 6)
        self.comboBox_2 = QComboBox(self.frame_5)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setEditable(False)

        self.verticalLayout_2.addWidget(self.comboBox_2)


        self.verticalLayout.addWidget(self.frame_5)
        
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMaximumSize(QSize(16777215, 10))
        self.progressBar.setToolTipDuration(-1)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)

        self.verticalLayout.addWidget(self.progressBar)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_9.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_9.addWidget(self.radioButton)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.listWidget = QListWidget(self.groupBox_2)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setSortingEnabled(False)

        self.horizontalLayout_4.addWidget(self.listWidget)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.treeView = QTreeView(self.groupBox_3)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setHeaderHidden(True)

        self.verticalLayout_5.addWidget(self.treeView)


        self.verticalLayout.addWidget(self.groupBox_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 20)
        self.tabWidget = QTabWidget(self.frame_6)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_7 = QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 400, -1)
        self.frame = QFrame(self.tab_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 4, -1, 4)
        self.comboBox_3 = QComboBox(self.frame)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_2.addWidget(self.comboBox_3)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.tab_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(9, 4, -1, 4)
        self.lineEdit = QLineEdit(self.frame_2)#search
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_5.addWidget(self.lineEdit)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.treeView_3 = QTreeView(self.tab_2)
        self.treeView_3.setObjectName(u"treeView_3")

        self.verticalLayout_7.addWidget(self.treeView_3)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_6 = QVBoxLayout(self.tab_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, 400, -1)
        self.frame_3 = QFrame(self.tab_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 4, -1, 4)
        self.comboBox_5 = QComboBox(self.frame_3)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.horizontalLayout_7.addWidget(self.comboBox_5)


        self.horizontalLayout_6.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.tab_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 4, -1, 4)
        self.lineEdit_3 = QLineEdit(self.frame_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_8.addWidget(self.lineEdit_3)


        self.horizontalLayout_6.addWidget(self.frame_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.treeView_4 = QTreeView(self.tab_3)
        self.treeView_4.setObjectName(u"treeView_4")

        self.verticalLayout_6.addWidget(self.treeView_4)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_3.addWidget(self.tabWidget)


        self.horizontalLayout_3.addWidget(self.frame_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        

        self.verticalLayout_4.addWidget(self.pushButton, 0, Qt.AlignRight)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.listWidget.setCurrentRow(-1)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Project", None))

        self.comboBox_2.setPlaceholderText("")
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Asset", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Shot", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Step Pipeline", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Model", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Layout", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Cfx", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Fx", None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Texture", None));
        ___qlistwidgetitem5 = self.listWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Rig", None));
        ___qlistwidgetitem6 = self.listWidget.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Anim", None));
        ___qlistwidgetitem7 = self.listWidget.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Light", None));
        ___qlistwidgetitem8 = self.listWidget.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Comp", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Entities", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Work", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Published", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
    # retranslateUi

