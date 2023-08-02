# import sys
# from PySide2.QtWidgets import QApplication, QMainWindow, QTreeView, QLineEdit
# from PySide2.QtCore import QSortFilterProxyModel, Qt
# from PySide2.QtGui import QStandardItemModel
# from PySide2.QtWidgets import QFileSystemModel

# class FileSearchProxyModel(QSortFilterProxyModel):
#     def filterAcceptsRow(self, sourceRow, sourceParent):
#         # Get the source index of the current row
#         sourceIndex = self.sourceModel().index(sourceRow, 0, sourceParent)
        
#         # Get the file name from the source model
#         fileName = self.sourceModel().data(sourceIndex, Qt.DisplayRole)
        
#         # Apply the filter based on the file name
#         filterRegExp = self.filterRegExp()
#         if filterRegExp.isEmpty():
#             return True
#         else:
#             return filterRegExp.pattern() in fileName

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.tree_view = QTreeView(self)
#         self.setCentralWidget(self.tree_view)

#         self.file_model = QFileSystemModel()
#         self.file_model.setRootPath(r"X:\pipeline\TestProject")  # Set the root directory path here

#         self.proxy_model = FileSearchProxyModel()
#         self.proxy_model.setSourceModel(self.file_model)
#         self.tree_view.setModel(self.proxy_model)

#         self.filter_input = QLineEdit(self)
#         self.filter_input.textChanged.connect(self.filter_changed)

#         self.setWindowTitle("File Explorer")

#     def filter_changed(self, text):
#         self.proxy_model.setFilterRegExp(text)
#         self.proxy_model.setFilterKeyColumn(0)  # Filter based on the first column (file name)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# sort = {
#         'Asset': {'Character':{'Woody', 'Buzz'}, 'Prop':{'ball', 'box'}, 'Environment':{'GasStation', 'PizzaPlanet'}},
#         'Shot': {'tpo_seq00_sh00':{'tpo_seq00'}, 'tpo_seq00_sh01':{'tpo_seq00'}}
#        }

# for item in sort.items():
#     for a in item:     
#         if isinstance(a, str):
#            print(a)
#         elif isinstance(a, dict):
#             for x in a.items():
#                 print(x)

# def print_hierarchy(data):
#     for key, value in data.items():
#         print(key)
#         if isinstance(value, dict):
#             print_hierarchy(value)
#         elif isinstance(value, set):
#             for item in value:
#                 print(item)

# sort = {
#     'Asset': {
#         'Character': {'Woody', 'Buzz'},
#         'Prop': {'ball', 'box'},
#         'Environment': {'GasStation', 'PizzaPlanet'}
#     },
#     'Shot': {
#         'tpo_seq00_sh00': {'tpo_seq00'},
#         'tpo_seq00_sh01': {'tpo_seq00'}
#     }
# }

# # print(type(sort))
# # # Print the hierarchy
# # print_hierarchy(sort)
# en_list = [{'type': 'Asset', 'code': 'Woody', 'sg_type': 'Character'},{'type': 'Asset', 'code': 'Buzz', 'sg_type': 'Character'},
#            {'type': 'Asset', 'code': 'ball', 'sg_type': 'Prop'},{'type': 'Asset', 'code': 'box', 'sg_type': 'Prop'},
#            {'type': 'Asset', 'code': 'GasStation', 'sg_type': 'Environment'},{'type': 'Asset', 'code': 'PizzaPlanet', 'sg_type': 'Environment'},
#            {'type': 'Shot', 'code': 'tpo_seq00_sh01', 'sg_type': 'tpo_seq00'},{'type': 'Shot', 'code': 'tpo_seq00_sh00', 'sg_type': 'tpo_seq00'}]
# sort = {}
# types = {}
# for typ in en_list:
#     sort[typ['type']] = {}
# print(sort)


# for dicts in en_list:
#     types[dicts['sg_type']] = {}
# print(types)
    
# def transform_list_to_dict(en_list):
#     transform_dict = {}

#     for item in en_list:
#         asset_type = item['type']
#         code = item['code']
#         sg_type = item['sg_type']

#         if asset_type not in transform_dict:
#             transform_dict[asset_type] = {}

#         if sg_type not in transform_dict[asset_type]:
#             transform_dict[asset_type][sg_type] = set()

#         transform_dict[asset_type][sg_type].add(code)

#     return transform_dict

# def print_hierarchy(data, sub=False):
#     for key, value in data.items():
#         if sub == True:
#             print('subkey :' + key)
#         print('key :' + key)     
           
#         if isinstance(value, dict):
#             print_hierarchy(value, True)
#         elif isinstance(value, set):
#             for item in value:
#                 print('item :' + item)

# en_list = [{'type': 'Asset', 'code': 'Woody', 'sg_type': 'Character'},
#            {'type': 'Asset', 'code': 'Buzz', 'sg_type': 'Character'},
#            {'type': 'Asset', 'code': 'ball', 'sg_type': 'Prop'},
#            {'type': 'Asset', 'code': 'box', 'sg_type': 'Prop'},
#            {'type': 'Asset', 'code': 'GasStation', 'sg_type': 'Environment'},
#            {'type': 'Asset', 'code': 'PizzaPlanet', 'sg_type': 'Environment'},
#            {'type': 'Shot', 'code': 'tpo_seq00_sh01', 'sg_type': 'tpo_seq00'},
#            {'type': 'Shot', 'code': 'tpo_seq00_sh00', 'sg_type': 'tpo_seq00'}]

# transformed_dict = transform_list_to_dict(en_list)
# print_hierarchy(transformed_dict)

# print(transformed_dict)


import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Replace 'data.json' with the path to your JSON file
file_path = r'C:\Users\High Tower\Documents\maya\2020\scripts\shotgrid.json'
json_data = read_json_file(file_path)

# Now, json_data will hold the content of the JSON file as a Python dictionary or list, depending on the file structure.
print(json_data["Project"])




