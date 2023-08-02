import maya.cmds as cmds
import maya.mel as mel
import maya.app.general.createImageFormats as createImageFormats

mel.eval('renderWindowRender redoPreviousRender renderView')
formatManager = createImageFormats.ImageFormats()
formatManager.pushRenderGlobalsForDesc("PNG")
cmds.renderWindowEditor('renderView', crc='camera1' ,com=True ,e=True, writeImage='X:/Maya_texture/testImage.png')
formatManager.popRenderGlobals()