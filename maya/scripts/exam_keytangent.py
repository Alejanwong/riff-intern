def mTranX(lin):
   
    Operate = 0
    Op = 0
    for Frame in range(0, 330, 30):
    
        cmds.setKeyframe('pCube1', attribute='translateX', t=(Frame,Frame))
        
        for Va in range(0, Operate+3, 2):
        
            cmds.setKeyframe('pCube1', attribute='translateX', t=(Frame,Frame), value=Va)
            Operate = Va        
    
    return 0        
    for Frame in range(0, lin*75, 60):
            
        cmds.setKeyframe('pCube1', attribute='translateX', t=(Frame,Frame))
                
        for Va in range(0, Op+3, 2):
        
            cmds.setKeyframe('pCube1', attribute='translateX', t=(Frame,Frame), value=Va*2)
            Op = Va
    
def mTranZ(rin):
    
    Operate = 0
    Op = 0
    for Frame in range(30, rin*75, 15):
    
        cmds.setKeyframe('pCube1', attribute='translateY', t=(Frame,Frame))
        
        for Va in range(45, rin*75, 60):
        
            cmds.setKeyframe('pCube1', attribute='translateY', t=(Va,Va), value=3)
                    
    
    return 0        
    for Frame in range(0, rin*75, 30):
            
        cmds.setKeyframe('pCube1', attribute='translateY', t=(Frame,Frame))
                
        for Va in range(0, Op+3, 2):
        
            cmds.setKeyframe('pCube1', attribute='translateY', t=(Frame,Frame), value=Va*2)
            Op = Va            

mTranX(4)
      