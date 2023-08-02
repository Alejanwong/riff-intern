import maya.cmds 

def cArrow(*args):
    cmds.curve(n='C_Arrow', d=1, p=[(-1,0,-1),(-1,0,-3),(-2,0,-3),(0,0,-5),(2,0,-3),
             (1,0,-3),(1,0,-1),(3,0,-1),(3,0,-2),(5,0,0),(3,0,2),(3,0,1),
             (1,0,1),(1,0,3),(2,0,3),(0,0,5),(-2,0,3),(-1,0,3),(-1,0,1),
             (-3,0,1),(-3,0,2),(-5,0,0),(-3,0,-2),(-3,0,-1),(-1,0,-1)])
    cmds.rename('curveShape1', 'cA_Ctrl') 
          
def PivotPoint(*args):
    
    pA = ['curveShape1','curveShape2','curveShape3','curveShape4'
          ,'curveShape5','curveShape6','curveShape7','curveShape8'] 
    Nx = 'arr{}.ry'
    Nz = 'ao{}.ry'
    k = 0
    
    cmds.circle(n='ppt', nr=(0,1,0), r=4) 
    
    for x in range(1, 5):       
          
        cmds.curve(n='arr1', d=1, p=[(-2,0,-5),(-1,0,-5),(0,0,-6),(1,0,-5),(2,0,-5)])        
        cmds.curve(n='ao1', d=1, p=[(5,0,2),(2,0,5)])
        for y in range(0, k+91, 90):
           
            cmds.setAttr(Nx.format(x), y)
            cmds.setAttr(Nz.format(x), y)
            k = y
    cmds.makeIdentity('arr1','arr2','arr3','arr4','ao1','ao2','ao3','ao4',a=True, t=1, r=1, s=1, n=2)
    cmds.parent(pA,'ppt',r=True,s=True)
    cmds.parent('arr1','arr2','arr3','arr4','ao1','ao2','ao3','ao4', rm=True)
    cmds.rename('ppt', 'PivotPoint_ctrl')
    
    for x in pA:
        cmds.rename(x, 'Ctrl_')
              
def Cube(*args):
    pA = ['topsq1Shape','leftsq1Shape','bottomsq1Shape','rightsq1Shape',
         'topsq2Shape','leftsq2Shape','bottomsq2Shape','rightsq2Shape',
         'curveShape1','curveShape2','curveShape3','curveShape4']
         
    cmds.nurbsSquare(n='sq1',nr=(0, 1, 0), sl1=2, sl2=2)
    cmds.nurbsSquare(n='sq2',nr=(0, 1, 0), sl1=2, sl2=2)
    cmds.setAttr('sq2.ty', 2)
    cmds.makeIdentity('sq2',a=True, t=1, r=1, s=1, n=2)
    cmds.curve(n='L1', d=1, p=[(1,0,-1),(1,2,-1)])
    cmds.curve(n='L2', d=1, p=[(1,0,1),(1,2,1)])
    cmds.curve(n='L3', d=1, p=[(-1,0,-1),(-1,2,-1)])
    cmds.curve(n='L4', d=1, p=[(-1,0,1),(-1,2,1)])
    cmds.parent(pA,'sq1',r=True,s=True)
    cmds.parent('topsq1','leftsq1','bottomsq1','rightsq1','sq2','L1','L2','L3','L4', rm=True)
    cmds.rename('sq1', 'Cube_ctrl')
    
    for x in pA:
        cmds.rename(x, 'Ctrl_')
  
def Pyramid(*args):
    pA = ['toppr1Shape','leftpr1Shape','bottompr1Shape','rightpr1Shape',
          'curveShape1','curveShape2','curveShape3','curveShape4']
    
    cmds.nurbsSquare(n='pr1',nr=(0, 1, 0), sl1=2, sl2=2)
    cmds.curve(n='pc1',d=1, p=[(1,0,-1),(0,2,0)])
    cmds.curve(n='pc2',d=1, p=[(1,0,1),(0,2,0)])
    cmds.curve(n='pc3',d=1, p=[(-1,0,-1),(0,2,0)])
    cmds.curve(n='pc4',d=1, p=[(-1,0,1),(0,2,0)])
    cmds.parent(pA,'pr1',r=True,s=True)
    cmds.parent('toppr1','leftpr1','bottompr1','rightpr1','pc2','pc3','pc4','pc1', rm=True)
    cmds.rename('pr1', 'Pyramid_ctrl')
    
    for x in pA:
        cmds.rename(x, 'Ctrl_')
  
def Sphere(*args):
    cmds.circle(n='ctrl0', nr=(1,0,0))
    cmds.circle(n='ctrl1', nr=(0,1,0))
    cmds.circle(n='ctrl2', nr=(0,0,1))
    cmds.parent('ctrl1Shape','ctrl2Shape','ctrl0',r=True,s=True)
    cmds.parent('ctrl1','ctrl2', rm=True)
    cmds.rename('ctrl0', 'Sphere_ctrl')

def CurveArrow(*args):
    pA = ['cc2Shape','curveShape1','curveShape2']

    cmds.circle(n='cc1', nr=(0, 1, 0), sw=180, r=3)
    cmds.circle(n='cc2', nr=(0, 1, 0), sw=180, r=3)
    cmds.setAttr('cc2.ty', 2)
    cmds.makeIdentity('cc2',a=True, t=1, r=1, s=1, n=2)
    cmds.curve(n='arrow1', d=1, p=[(0,0,3),(0,-1,3),(2,1,3),(0,3,3),(0,2,3)])
    cmds.curve(n='arrow1', d=1, p=[(0,0,-3),(0,-1,-3),(2,1,-3),(0,3,-3),(0,2,-3)])
    cmds.parent(pA,'cc1',r=True,s=True)
    cmds.parent('cc2','arrow1','arrow2', rm=True)
    cmds.rename('cc1', 'CurveArrow_ctrl')
    cmds.rename('curveShape1', 'CurveAr_ctrl')
    cmds.rename('curveShape2', 'CurveAr_ctrl')
 
def MergeCtrl(*args):
    cmds.parent(r=True,s=True)
      
cmds.window()
cmds.rowColumnLayout(numberOfColumns=3, cs=[(1,5),(2,5),(3,5)], cw=[(1,150),(2,150),(3,150)], rs=[(1,5),(2,5)])
cmds.button(label='CrossArrow', command=cArrow, h=100)  
cmds.button(label='Cube', command=Cube)
cmds.button(label='Pyramid', command=Pyramid)
cmds.button(label='Sphere', command=Sphere, h=100)
cmds.button(label='CurveArrow', command=CurveArrow)
cmds.button(label='PivotPoint', command=PivotPoint)
cmds.button(label='MergeCtrl', command=MergeCtrl)
cmds.showWindow()

  
