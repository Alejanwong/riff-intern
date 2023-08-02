import maya.cmds 
from os import mkdir, listdir

def get_shader():    
    Ks = cmds.ls(sl=True, st=False, modified=True)    
    com = ['coverage','translateFrame','rotateFrame','mirrorU','mirrorV','stagger',
           'wrapU','wrapV','repeatUV','offset','rotateUV','noiseUV','vertexUvOne',
           'vertexUvTwo','vertexUvThree','vertexCameraOne']
           
    pSh = '{}_Shader'
    pSk = '{}SG'
    pfile = '{}.{}'
    xfile = '{}.{}'
    path = "X:/Maya_texture/{}"
    
    for x in Ks:        
        cmds.sets(name=pSk.format(x), renderable=True, empty=True)
        cmds.shadingNode('aiStandardSurface', name=pSh.format(x), asShader=True)
        cmds.surfaceShaderList(pSh.format(x), add=pSk.format(x))
        cmds.sets(x, e=True, forceElement=pSk.format(x))
        cmds.shadingNode('file', n='{}_file'.format(x), at=True, icm=True) 
        cmds.shadingNode('place2dTexture', n='{}_place2dTexture'.format(x), au=True)
        cmds.connectAttr(pfile.format('{}_place2dTexture'.format(x),'outUV'), xfile.format('{}_file'.format(x),'uv'))
        cmds.connectAttr(pfile.format('{}_place2dTexture'.format(x),'outUvFilterSize'), xfile.format('{}_file'.format(x),'uvFilterSize'))
        cmds.connectAttr(xfile.format('{}_file'.format(x),'outColor'), pfile.format(pSh.format(x), 'baseColor'))              
        mkdir(path.format(pSh.format(x)))
        
        for i in com:
            cmds.connectAttr(pfile.format('{}_place2dTexture'.format(x),i), xfile.format('{}_file'.format(x),i), f=True)         
        
def get_texture():
    pSh = '{}_Shader'
    path = "X:/Maya_texture/{}/"
    Ks = cmds.ls(sl=True, st=False, modified=True)
    
    for p in Ks:        
        fList = listdir(path.format(pSh.format(p)))
        print(pSh.format(p), fList)    
        cmds.setAttr('{}_file.fileTextureName'.format(p), path.format(pSh.format(p))+fList[0], type="string")   
   
cmds.window()
cmds.rowColumnLayout(numberOfColumns=2, cs=[(1,5),(2,5),(3,5)], cw=[(1,150),(2,150),(3,150)], rs=[(1,5),(2,5)])
cmds.button(l='Create Shader', h=100, c='get_shader()')
cmds.button(l='Set Texture', c='get_texture()')
cmds.showWindow()