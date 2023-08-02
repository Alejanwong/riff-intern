import maya.cmds as cmds
import maya.utils as utils
import os
import sys

sys.path.append(r"C:\Users\High Tower\Documents\maya\2020\scripts\subfolder")

def autoRun():
    script_path = '<path_to_your_script>'   
    load_path = os.environ.get('LOAD_PATH')
    if load_path == '':
        return
    
    open_port()
    import_file(load_path)
        
def open_port():
    # commandPort -name "localhost:7001" -sourceType "mel" -echoOutput
    cmds.commandPort(n="localhost:7001", stp="mel", eo=True)
 
    
def import_file(file_path):
    cmds.file(new=True, force=True)      
    cmds.file(file_path, i=True, ignoreVersion=True, mergeNamespacesOnClash=False, namespace=":")
    print('=======================================\n')
    print('|         File success loaded         |\n')
    print('=======================================\n')

utils.executeDeferred(autoRun)




