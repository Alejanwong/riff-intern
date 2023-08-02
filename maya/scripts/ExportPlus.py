import os
import json
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent
from PySide2.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance
import maya.OpenMayaUI as ui 

from ExportPlus_ui import Ui_MainWindow
from ExportPlus_maya import *
from fetch_api import fetcher

# _DIRNAME_ = os.path.dirname(__file__)


class ExportPlus(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(ExportPlus, self).__init__(parent)
        self.setupUi(self)
        self.preset_file = r'C:\Users\High Tower\Documents\maya\2020\scripts\exportplus_preset.json'
        self.preset_data = self.read_json_file(self.preset_file)
        self.query = fetcher() 
        self.query.load_all()
        self.comboBox_2.addItems(self.query.entity_list())
        self.comboBox.addItems(self.query.project_list())
        self.comboBox.activated.connect(self.project_sel)
        self.comboBox_2.activated.connect(self.enitity_sel)
        self.radioButton.clicked.connect(lambda: self.export_sel(self.radioButton.text()))
        self.radioButton_3.clicked.connect(lambda: self.export_sel(self.radioButton_3.text()))
        self.radioButton_4.clicked.connect(lambda: self.export_sel(self.radioButton_4.text()))
        self.radioButton_5.clicked.connect(lambda: self.export_sel(self.radioButton_5.text()))
        self.pushButton_3.clicked.connect(self.execute_export)
        
    def read_json_file(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
        
    def export_sel(self, export):
        # print(export)
        self.listWidget.clear()
        
        for preset in self.preset_data[export]:
            # print(preset)
            item_widget = QCheckBox(preset)
            list_item = QListWidgetItem()
            self.listWidget.addItem(list_item)
            self.listWidget.setItemWidget(list_item, item_widget)
            item_widget.clicked.connect(lambda: self.preset_sel(item_widget.text()))
        
        
        
        if self.radioButton.isChecked():#model
            self.param = ['abc','model']
        elif self.radioButton_3.isChecked():#lookdev
            self.param = ['ma','lookdev']
        elif self.radioButton_4.isChecked():#rig
            self.param = ['ma','rig']
        elif self.radioButton_5.isChecked():#anim
            self.param = ['abc','anim']      
            
    def project_sel(self, index):
        self.project = self.comboBox.itemText(index)
        
    def enitity_sel(self, index):
        self.entity = self.comboBox_2.itemText(index)
        
    def preset_sel(self, preset):
        list_preset = []
        list_preset.append(preset)
        print(list_preset)
        
    
    def execute_export(self):
        self.query.get_step(self.param[1])
        part = self.query.merge_data()
        # print(part)
        for pa in part:
            if self.entity == pa['code']:
                entity_type = pa['sg_type']
                types = pa['type']
                
        
        # X:\pipeline\TestProject\Asset\Character\BuzzLighyear\version_01\anim\BuzzLighyear.abc
        
        path = r"X:/pipeline/{}/{}/{}/{}/version_01/{}/{}".format(self.project, types, entity_type, self.entity, self.param[1], '{}_{}_{}.{}'.format(self.project, self.param[1], self.entity, self.param[0]))
        anim_path = r"X:/pipeline/{}/{}/{}/{}/version_01/{}/{}".format(self.project, types, entity_type, self.entity, 'anim', '{}_{}_{}.{}'.format(self.project, 'anim', self.entity, self.param[0]))
        model_path = r"X:/pipeline/{}/{}/{}/{}/version_01/{}/{}".format(self.project, types, entity_type, self.entity, 'model', '{}_{}_{}.{}'.format(self.project, 'model', self.entity, self.param[0]))
        print(path)
        command = 'export_{}_{}'.format(self.param[0],self.param[1])
        func = eval(command)
        func(path, anim_path, model_path)
           
def getAddr():   
    addr = ui.MQtUtil.mainWindow()
    mayaUI = wrapInstance(int(addr), QWidget)
    return mayaUI                                

if __name__ == '__main__':
    # if not QApplication.instance():
    #     app = QApplication(sys.argv)
    # else:
    #     app = QApplication.instance()
    window = ExportPlus(getAddr())
    window.show()

