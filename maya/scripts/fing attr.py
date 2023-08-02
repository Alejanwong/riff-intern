#k = cmds.listAttr()
#print (k)
#cmds.ls(st=False, modified=True)
#cmds.setAttr('pSphere1_file.file', 'C:/Users/High Tower/Documents/maya/projects/default/sourceimages/Rebellion.jpg')

list = cmds.ls(type='file')
for node in list:
    print cmds.getAttr(node+'.fileTextureName')