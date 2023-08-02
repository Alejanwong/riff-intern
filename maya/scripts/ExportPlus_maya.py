import maya.cmds as cmds


def export_abc_model(path, anim_path, model_path):
    root = 'main_model'
    
    objlist = cmds.ls(tr=True)    
    if root in objlist:
        command = "-frameRange 0 0 -uvWrite -worldSpace -root {} -file {}".format(root, path)
        cmds.AbcExport(j=command)
    else:
        cmds.error('Main group ' + root + ' not found')
    
    print("---Export Secceses---")        

def export_ma_lookdev(path, anim_path, model_path):
    root = 'main_lookdev'
    file_type = "mayaAscii"
       
    objlist = cmds.ls(type='shadingEngine')
    for shadingEngine in objlist:
        shader = cmds.listConnections(shadingEngine + '.surfaceShader')
        if shader[0] == root: 
            # if not "{}.model".format(root) and "{}.anim".format(root): 
            #     cmds.setAttr("{}.model".format(root), model_path, type="string")
            #     cmds.setAttr("{}.anim".format(root), anim_path, type="string")
            cmds.select(root)
            cmds.addAttr(longName="model", dataType="string") 
            cmds.addAttr(longName="anim", dataType="string")
            cmds.setAttr("{}.model".format(root), model_path, type="string")
            cmds.setAttr("{}.anim".format(root), anim_path, type="string")
            cmds.file(path, exportSelected=True, type=file_type, force=True)
            print("---Export Secceses---")  
            
      

def export_ma_rig(path, anim_path, model_path):
    root = 'main_rig'
    file_type = "mayaAscii"
    
    objlist = cmds.ls(tr=True)    
    if root in objlist:
        cmds.select(root)
        cmds.file(path, exportSelected=True, type=file_type, force=True)
    else:
        cmds.error('Main group ' + root + ' not found')
        
    print("---Export Secceses---")
    
def export_abc_anim(path, anim_path, model_path):
    root = 'main_anim'
    
    objlist = cmds.ls(tr=True)  
    print(objlist)  
    start = cmds.playbackOptions(query=True, minTime=True)
    end = cmds.playbackOptions(query=True, maxTime=True)
    
    if root in objlist:
        command = "-frameRange {} {} -uvWrite -worldSpace -root {} -file {}".format(start, end, root, path)
        cmds.AbcExport(j=command)
    else:
        cmds.error('Main group ' + root + ' not found')

    print("---Export Secceses---")

# print('===============================')