import maya.cmds as cmds

k = cmds.ls(sl=True, type='joint')

for i in k:
    cmds.parentConstraint(i, cmds.circle(nr=(1,0,0), n=i+'_Ctrl'))
    cmds.delete(i+'_Ctrl'+'_parentConstraint1')
    cmds.makeIdentity(i+'_Ctrl', a=True, t=1, r=1, s=1, n=2)
    cmds.parentConstraint(i+'_Ctrl', i, mo=True)
                             
for ap_row in range(len(k)-1):                  
    for p_row in range(1):    
        cmds.parent(k[ap_row]+'_Ctrl', k[ap_row+1]+'_Ctrl')
             
