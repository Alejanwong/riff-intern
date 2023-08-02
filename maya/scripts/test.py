# import os

# def make_hierarchy_directory(base_path, hierarchy_structure):
#     """
#     Create a hierarchical directory structure.

#     Args:
#         base_path (str): The base path where the hierarchy will be created.
#         hierarchy_structure (list): List representing the hierarchical structure.
#                                     Each element in the list is a directory name.

#     Returns:
#         str: The final path of the created directory.
#     """
#     # Combine the base path and the elements of the hierarchy structure
#     full_path = os.path.join(base_path, *hierarchy_structure)

#     # Create the directory if it doesn't exist
#     os.makedirs(full_path, exist_ok=True)

#     return full_path

# if __name__ == "__main__":
#     base_path = r"X:\pipeline\New folder"  # Replace this with the desired base path
#     hierarchy_structure = ["folder1", "folder2", "folder3"]  # Replace this with your hierarchy

#     final_directory = make_hierarchy_directory(base_path, hierarchy_structure)
#     print(f"Created hierarchical directory: {final_directory}")

#==========================================================================================

# import sys
# import json
# from PySide2.QtWidgets import QApplication, QListWidget, QListWidgetItem, QVBoxLayout, QWidget

# def read_json_file(file_path):
#     with open(file_path, 'r') as file:
#         data = json.load(file)
#     return data

# def main():
#     app = QApplication(sys.argv)

#     # Create the main application window
#     window = QWidget()
#     window.setWindowTitle('QListWidget with JSON Data')
#     window.setGeometry(100, 100, 300, 200)

#     # Create a QListWidget
#     list_widget = QListWidget()

#     # Read data from the JSON file
#     file_path = 'data.json'
#     data = read_json_file(file_path)

#     # Add items to the QListWidget
#     for key, value in data.items():
#         item_text = f'{key}: {value}'
#         list_item = QListWidgetItem(item_text)
#         list_widget.addItem(list_item)

#     # Create a layout and add the QListWidget to it
#     layout = QVBoxLayout()
#     layout.addWidget(list_widget)

#     # Set the layout for the main window
#     window.setLayout(layout)

#     # Show the main window
#     window.show()

#     # Execute the application
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# #==========================================================================================

# import sys
# from PySide2.QtWidgets import QApplication, QListWidget, QListWidgetItem, QVBoxLayout, QCheckBox, QWidget

# def main():
#     app = QApplication(sys.argv)

#     # Create the main application window
#     window = QWidget()
#     window.setWindowTitle('QListWidget with Checkboxes')
#     window.setGeometry(100, 100, 300, 200)

#     # Create a QListWidget
#     list_widget = QListWidget()

#     # Add items to the QListWidget with checkboxes
#     items = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']
#     for item_text in items:
#         # Create a QListWidgetItem with a QCheckBox as its widget
#         item_widget = QCheckBox(item_text)
#         list_item = QListWidgetItem()
#         list_widget.addItem(list_item)
#         list_widget.setItemWidget(list_item, item_widget)

#     # Create a layout and add the QListWidget to it
#     layout = QVBoxLayout()
#     layout.addWidget(list_widget)

#     # Set the layout for the main window
#     window.setLayout(layout)

#     # Show the main window
#     window.show()

#     # Execute the application
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# #=====================================

# import maya.cmds as cmds

# def import_alembic_cache(alembic_file_path):
#     # Import the Alembic cache file
#     cmds.file(alembic_file_path, i=True, type="Alembic", rnn=True)

# def connect_lookdev_with_ascii(maya_ascii_file_path):
#     # Open the Maya ASCII file
#     cmds.file(maya_ascii_file_path, o=True, f=True)

#     # Get the shading engines (materials) in the scene
#     shading_engines = cmds.ls(type='shadingEngine')
#     print(shading_engines)
    
#     # Connect the shading engines to the mesh objects in the Alembic cache
#     for shading_engine in shading_engines:
#         mesh_objs = cmds.sets(shading_engine, q=True)
#         if not mesh_objs:
#             continue

#         # for mesh_obj in mesh_objs:
#         #     # Check if the mesh object exists in the scene
#         #     if cmds.objExists(mesh_obj):
#         #         # Connect the shading engine to the mesh
#         #         cmds.sets(mesh_obj, e=True, forceElement=shading_engine)
#         #     else:
#         #         print(f"Warning: Mesh object '{mesh_obj}' not found in the scene.")

# # if __name__ == "__main__":
# # Replace with the path to your Alembic cache file (.abc)
# alembic_file_path = r"X:\pipeline\TestProject\Asset\Character\Woody\version_01\anim\Woody.abc"

# # Replace with the path to your Maya ASCII file (.ma)
# maya_ascii_file_path = r"X:\pipeline\TestProject\Asset\Character\Woody\version_01\lookdev\Woody.ma"

# # Import the Alembic cache
# import_alembic_cache(alembic_file_path)

# # Connect the lookdev from the Maya ASCII file to the Alembic cache
# connect_lookdev_with_ascii(maya_ascii_file_path)

# cmds.getAttr('aiStandardSurface1.anim')

# path = "X:/pipeline/TestProject/Asset/Character/BuzzLighyear/version_01/anim/TestProject_anim_BuzzLighyear.abc"
# anim_path = path.split("/")
# file_name = anim_path[-1].split('_')
# print(anim_path)
# print(file_name)

# file -import -type "mayaAscii"  -ignoreVersion -ra true -mergeNamespacesOnClash false 
# -namespace "TestProject_lookdev_Rex" -options "v=0;"  -pr  -importFrameRate true  
# -importTimeRange "override" "X:/pipeline/TestProject_lookdev_Rex.ma";

# import maya.cmds as cmds
# cmds.file("X:/pipeline/shade.ma", i=True, typ="mayaAscii", iv=True, ra=True, mnc=False, ns='shade', op="v=0;", pr=True)


# import json

# def read_json_file(file_path):
#     with open(file_path, 'r') as file:
#         data = json.load(file)
#     return data

# # Replace 'data.json' with the path to your JSON file
# file_path = r'C:\Users\High Tower\Documents\maya\2020\scripts\shotgrid.json'
# json_data = read_json_file(file_path)

# # Now, json_data will hold the content of the JSON file as a Python dictionary or list, depending on the file structure.
# print(json_data)

def test():
    anim_path = r"X:/pipeline/{}/{}/{}/{}/version_01/anim/{}"
    shade_path = r"X:/pipeline/{}/{}/{}/{}/version_01/anim/{}"
            
    return anim_path, shade_path

t = test()
print(t[0])

# for x in test():
    
#     print(x[0])

