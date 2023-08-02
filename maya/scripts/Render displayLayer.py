import maya.cmds 
import maya.mel as mel
import maya.app.general.createImageFormats as createImageFormats
        
def close_layer():
    sL = cmds.ls(modified=True, type='displayLayer')
    vi = '{}.visibility'
        
    for x in sL:        
        cmds.setAttr(vi.format(x), 0)
    render_player()        
    
def render_player():
    
    sL = cmds.ls(st=True, modified=True, type='displayLayer')
    vi = '{}.visibility'
    
    for x in sL:
        sL.remove(u'displayLayer')
        cmds.setAttr(vi.format(x), 1)        
        mel.eval('renderWindowRender redoPreviousRender renderView')
        formatManager = createImageFormats.ImageFormats()
        formatManager.pushRenderGlobalsForDesc("PNG")
        cmds.renderWindowEditor('renderView', crc='camera1' ,com=True ,e=True, writeImage='X:/Maya_texture/{}.png'.format(x))
        formatManager.popRenderGlobals()
        cmds.setAttr(vi.format(x), 0)
   
close_layer()

    
    




    
    
    