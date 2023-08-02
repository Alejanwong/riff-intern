import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QTreeView
#from PySide2.QtCore import 
from PySide2.QtGui import QFont, QColor, QStandardItemModel, QStandardItem


class StandardItem(QStandardItem):
    def __init__(self, txt='', font_size=12, set_bold=False, color=QColor(0, 0, 0)):
        super().__init__()

        fnt = QFont('Open Sans', font_size)
        fnt.setBold(set_bold)

        self.setEditable(True)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)


class AppDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('World Country Diagram')
        self.resize(500, 700)

        treeView = QTreeView()
        treeView.setHeaderHidden(True)

        treeModel = QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()

        california = StandardItem('California', 14)
        
        la = StandardItem('Los angle', 12)
        california.appendRow(la)
        treeModel.findItems(obj['type'])
        ny = StandardItem('New York', 12)
        california.appendRow(ny)
        # America
        america = StandardItem('America', 16, set_bold=True)

        
        america.appendRow(california)
        rootNode.appendRow(america)
        
        dc = StandardItem('DC', 12)
        california.appendRow(dc)
        # oakland = StandardItem('Oakland', 12, color=QColor(155, 0, 0))
        # sanfrancisco = StandardItem('San Francisco', 12, color=QColor(155, 0, 0))
        # sanjose = StandardItem('San Jose', 12, color=QColor(155, 0, 0))
    #     city = ['Oakland','San Francisco','San ose']
    #     for x in city:
            
    #         obj = StandardItem(x, 12, color=QColor(155, 0, 0))

    #         california.appendRow(obj)
    #     # california.appendRow(sanfrancisco)
    #     # california.appendRow(sanjose)


    #     texas = StandardItem('Texas', 14)
    #     america.appendRow(texas)

    #     austin = StandardItem('Austin', 12, color=QColor(155, 0, 0))
    #     houston = StandardItem('Houston', 12, color=QColor(155, 0, 0))
    #     dallas = StandardItem('dallas', 12, color=QColor(155, 0, 0))

    #     texas.appendRow(austin)
    #     texas.appendRow(houston)
    #     texas.appendRow(dallas)


    #     # Canada 
    #     canada = StandardItem('America', 16, set_bold=True)

    #     alberta = StandardItem('Alberta', 14)
    #     bc = StandardItem('British Columbia', 14)
    #     ontario = StandardItem('Ontario', 14)
    #     canada.appendRows([alberta, bc, ontario])


        # rootNode.appendRow(america)
    #     rootNode.appendRow(canada)

        treeView.setModel(treeModel)
        treeView.expandAll()
    #     treeView.doubleClicked.connect(self.getValue)

        self.setCentralWidget(treeView)

    # def getValue(self, val):
    #     print(val.data())
    #     print(val.row())
    #     print(val.column())


app = QApplication(sys.argv)        

demo = AppDemo()
demo.show()

sys.exit(app.exec_())
