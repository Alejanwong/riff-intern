from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent
from PySide2.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance
import maya.OpenMayaUI as ui 

from BuilderPlus_ui import Ui_MainWindow
from BuilderPlus_maya import *
from fetch_api import fetcher

class BuilderPlus(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(BuilderPlus, self).__init__(parent)
        self.setupUi(self)
        self.query = fetcher() 
        self.query.load_all()
        self.build_shot = build_shot()
        self.build_asset = build_asset()
        self.pushButton.clicked.connect(self.build_execute_shot)#build shot
        self.pushButton_2.clicked.connect(self.build_execute_asset)#build asset
        self.comboBox_2.addItems(self.query.project_list())#project list shot page  
        self.comboBox_3.addItems(self.query.project_list())#project list asset page 
        # self.comboBox_4.addItems(self.query.entity_list())   
        # self.comboBox.activated.connect(self.project_sel)
        self.comboBox_2.activated.connect(self.shot_page)#shot page
        self.comboBox_3.activated.connect(self.asset_page)#asset page 
        # self.comboBox_4.activated.connect(self.project_sel)
    
    def shot_page(self, index):
        self.project = self.comboBox_2.itemText(index)
        self.project_sel('shot')
        
    def asset_page(self, index):
        self.project = self.comboBox_3.itemText(index)
        self.project_sel('asset')
        
    def project_sel(self, page):
        if page == 'shot':     
            self.listWidget.clear()
            self.listWidget.addItems(self.query.shot_list())
            self.listWidget.itemClicked.connect(self.shot_sel)
        else:
            self.listWidget_2.clear()
            self.listWidget_2.addItems(self.query.entity_list())
            self.listWidget_2.itemClicked.connect(self.asset_sel)
    
    def shot_sel(self, item):
        self.shot = item.text().lower()
        shot_data = self.query.shot_data()
        
        self.asset = []
        for shot in shot_data:
            if self.shot == shot['code']:
                for asset_name in shot['assets']:
                    self.asset.append(asset_name['name'])
        # print(self.asset)
        
    def asset_sel(self, item):
        self.entity = item.text()
        asset_data = self.query.asset_data()
        
        
    def build_execute_shot(self):
        for asset_name in self.asset:
            path = self.gen_path(asset_name)
            self.build_shot.abc_shade_anim(path[0], path[1], asset_name)
    
    def build_execute_asset(self):   
        asset_name = self.entity  
        path = self.gen_path(asset_name)
        self.build_asset.abc_shade(path[0], path[2], asset_name)
        print("{} | {}".format(path[0], path[2]))    
        
    def gen_path(self, objname):
        asset_data = self.query.asset_data()
        for asset in asset_data:
            if objname == asset["code"]:
                asset_type = asset["sg_asset_type"] 
        
        # X:\pipeline\TestProject\Asset\Character\BuzzLighyear\version_01\anim\BuzzLighyear.abc
        anim_path = r"X:/pipeline/{}/Asset/{}/{}/version_01/anim/{}".format(self.project, asset_type, objname, '{}_{}_{}.abc'.format(self.project, 'anim', objname))
        shade_path = r"X:/pipeline/{}/Asset/{}/{}/version_01/lookdev/{}".format(self.project, asset_type, objname, '{}_{}_{}.ma'.format(self.project, 'lookdev', objname))
        model_path = r"X:/pipeline/{}/Asset/{}/{}/version_01/model/{}".format(self.project, asset_type, objname, '{}_{}_{}.abc'.format(self.project, 'model', objname))
        
        return shade_path, anim_path, model_path
                

def getAddr():   
    addr = ui.MQtUtil.mainWindow()
    mayaUI = wrapInstance(int(addr), QWidget)
    return mayaUI                                

if __name__ == '__main__':
    window = BuilderPlus(getAddr())
    window.show()