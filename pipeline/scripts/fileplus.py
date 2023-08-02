from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore
import subprocess
import os

from ui import main
from fetch_api import fetcher

__DIRNAME__ = os.path.dirname(__file__)

class MyFileBrowser(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self, maya=True):
        super(MyFileBrowser, self).__init__()
        self.setupUi(self)
        self.maya = maya
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.context_menu)
        self.listWidget.itemClicked.connect(self.step_sel)
        self.query = fetcher()
        self.comboBox_2.addItems(self.query.project_list())
        self.comboBox_2.activated.connect(self.project_sel)
        self.radioButton.clicked.connect(self.sel_filter)
        self.radioButton_2.clicked.connect(self.sel_filter)
        self.pushButton.clicked.connect(self.setting_env)
        self.lineEdit.textChanged.connect(self.filter_changed)
    
    def setting_env(self):
        index = self.treeView_3.currentIndex()
        file_path = self.model.filePath(index)
        f = open(r"C:\Users\High Tower\Documents\maya\2020\Maya.env", "w")
        f.write("LOAD_PATH = {}".format(file_path))
        f.close()
        
        self.runMaya()
        
    def runMaya(self):
        # "X:\pipeline\scripts\program\Maya 2020.lnk"
        path = r"{}\program\Maya 2020.lnk".format(__DIRNAME__)       
        command = ["cmd", "/c", "start", "", path]
        subprocess.run(command, shell=True)
        
    def project_sel(self, index):
        
        self.query.get_project(self.comboBox_2.itemText(index))
        
    # def progressbar_state(self):
    #     self.progressBar.setValue(0)
    
    def step_sel(self, item):
        self.step = item.text().lower()
        # print(self.step)
        self.query.get_step(self.step)
        self.query.transform()
        # self.create_data()
        self.show_entity()
        
    def filter_changed(self, text):
        self.proxy_model.setFilterRegExp(text)
        self.proxy_model.setFilterKeyColumn(0)
    
    def create_model(self, data, sub=False):
        for key, value in data.items():
            if sub == True:
                #subkey
                self.sub_type = QtGui.QStandardItem(key)
                self.sub_type.setEditable(False)
                self.obj_type.appendRow(self.sub_type)
            elif sub == False:
                #mainkey
                self.obj_type = QtGui.QStandardItem(key) 
                self.obj_type.setEditable(False)              
                self.rootNode.appendRow(self.obj_type)     
            
            if isinstance(value, dict):
                self.create_model(value, True)
            elif isinstance(value, set):
                for item in value:
                    self.obj_name = QtGui.QStandardItem(item)
                    self.obj_name.setEditable(False)
                    self.sub_type.appendRow(self.obj_name)
    
    def show_entity(self):
        data = self.query.transform()
        self.treeModel = QtGui.QStandardItemModel()
        self.rootNode = self.treeModel.invisibleRootItem()
        
        self.create_model(data)
                    
        self.treeView.setModel(self.treeModel)
        self.treeView.expandAll()
        self.treeView.doubleClicked.connect(self.gotofile)
           
    def create_data(self):
        # self.fetch = self.query.merge_data()
        # print(self.fetch)
        self.treeModel = QtGui.QStandardItemModel()
        self.rootNode = self.treeModel.invisibleRootItem()
              
        obj_old = []
        
        if self.sel_filter() == 'asset':
            print('asset')
        elif self.sel_filter() == 'shot':
            print('shot')
            
        for obj in self.fetch:   
            # print(obj_old)       
            main_items = self.treeModel.findItems(obj['type'])                      
            if not main_items:               
                obj_type = QtGui.QStandardItem(obj['type'])               
                self.rootNode.appendRow(obj_type)

            if not obj['sg_type'] in obj_old: 
                sub_type = QtGui.QStandardItem(obj['sg_type'])
                obj_type.appendRow(sub_type)
                # obj_old = obj['sg_type']
                obj_old.append(obj['sg_type'])
                
            obj_name = QtGui.QStandardItem(obj['code'])
            sub_type.appendRow(obj_name)
            
                    
        self.treeView.setModel(self.treeModel)
        self.treeView.expandAll()
        self.treeView.doubleClicked.connect(self.gotofile)
        
    def sel_filter(self):
        # self.treeModel = QtGui.QStandardItemModel()
        # self.rootNode = self.treeModel.invisibleRootItem()
       
        obj_old = ''
        button_state = ''
        if self.radioButton.isChecked():#Shot
            # for obj in self.fetch:   
            #     if obj['type'] == 'Shot':
            #         if not obj['sg_type'] == obj_old:
            #             sub_type = QtGui.QStandardItem(obj['sg_type'])
            #             self.rootNode.appendRow(sub_type)
            #             obj_old = obj['sg_type']
                        
            #         obj_name = QtGui.QStandardItem(obj['code'])
            #         sub_type.appendRow(obj_name) 
            button_state = 'shot'   
            return button_state
        elif self.radioButton_2.isChecked():#Asset
            # for obj in self.fetch:   
            #     if obj['type'] == 'Asset':
            #         if not obj['sg_type'] == obj_old:
            #             sub_type = QtGui.QStandardItem(obj['sg_type'])
            #             self.rootNode.appendRow(sub_type)
            #             obj_old = obj['sg_type']
                        
            #         obj_name = QtGui.QStandardItem(obj['code'])
            #         sub_type.appendRow(obj_name)   
            button_state = 'asset'   
            return button_state
        # self.treeView.setModel(self.treeModel)
        # self.treeView.expandAll()
        # self.treeView.doubleClicked.connect(self.gotofile)
        
                                                                           
    def gotofile(self, val):
        self.fetch = self.query.merge_data()
        for paths in self.fetch:
            if paths['code'] == val.data():
                path = r"X:\pipeline\TestProject\{}\{}\{}\version_01\{}".format(paths['type'], paths['sg_type'], paths['code'], self.step)
            
        print(path)
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath((QtCore.QDir.rootPath()))
        # self.proxy_model = QtCore.QSortFilterProxyModel()
        # self.proxy_model.setSourceModel(self.model)
        self.treeView_3.setModel(self.model)
        self.treeView_3.setRootIndex(self.model.index(path))
        self.treeView_3.setSortingEnabled(True)
        

    def context_menu(self):
        menu = QtWidgets.QMenu()
        open = menu.addAction("Open in new maya")
        open.triggered.connect(self.open_file)

        if self.maya:
            open_file = menu.addAction("Open file")
            open_file.triggered.connect(lambda: self.maya_file_operations(open_file=True))

            import_to_maya = menu.addAction("Import to Maya")
            import_to_maya.triggered.connect(self.maya_file_operations)

            reference_to_maya = menu.addAction("Add reference to Maya")
            reference_to_maya.triggered.connect(lambda: self.maya_file_operations(reference=True))

        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())

    def open_file(self):
        index = self.treeView_3.currentIndex()
        file_path = self.model.filePath(index)
        os.startfile(file_path)

    def maya_file_operations(self, reference=False, open_file=False):

        index = self.treeView_3.currentIndex()
        file_path = self.model.filePath(index)
        import maya.cmds as cmds
        if reference:
            cmds.file(file_path, reference=True, type='mayaAscii', groupReference=True)
        elif open_file:
            file_location = cmds.file(query=True, location=True)
            if file_location == 'unknown':
                cmds.file(file_path, open=True, force=True)
            else:
                modify_file = cmds.file(query=True, modified=True)
                if modify_file:
                    result = cmds.confirmDialog(title='Opening new maya file',
                                                message='This file is modified. do you want to save this file.?',
                                                button=['yes', 'no'],
                                                defaultButton='yes',
                                                cancelButton='no',
                                                dismissString='no')
                    if result == 'yes':
                        cmds.file(save=True, type='mayaAscii')
                        cmds.file(file_path, open=True, force=True)
                    else:
                        cmds.file(file_path, open=True, force=True)
                else:
                    cmds.file(file_path, open=True, force=True)
        else:
            cmds.file(file_path, i=True, groupReference=True)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    fb = MyFileBrowser()
    fb.show()
    app.exec_()