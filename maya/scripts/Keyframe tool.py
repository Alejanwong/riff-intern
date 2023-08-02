import maya.cmds 

class Graph:
    
    def Popup_menu(self, page):        
        self.p = page   
         
        if self.p == 1:           
           com = 'graph_creater.C_linear()'                    
        elif self.p == 2:
           com = 'graph_creater.C_UpSlope()'           
        elif self.p == 3:
           com = 'graph_creater.C_DownSlope()'              
        elif self.p == 4:
           com = 'graph_creater.C_Wave()'             
        elif self.p == 5:
           com = 'graph_creater.C_Bouncing()'
                           
        #return 0               
        cmds.window()
        cmds.columnLayout()
        self.St_val = cmds.intFieldGrp(numberOfFields=1, label='Start')
        self.End_val = cmds.intFieldGrp(numberOfFields=1, label='End')
        self.Va_val = cmds.intFieldGrp(numberOfFields=1, label='Value')
        self.Point_val = cmds.intFieldGrp(numberOfFields=1, label='Point')
        self.attr = cmds.checkBoxGrp(numberOfCheckBoxes=3, label='Attibutes', labelArray3=['Translate', 'Rotate', 'Scale'])
        self.axle = cmds.checkBoxGrp(numberOfCheckBoxes=3, label='Axle', labelArray3=['X', 'Y', 'Z'])              
        cmds.button(label='Create', c=com)
        cmds.showWindow() 
 
    def C_linear(self):
        
        graph_creater.Post_val()                       
        mkP = (self.End_lin + self.St_lin) / self.Point_lin
                
        for i in range(self.St_lin, self.End_lin+1, mkP):                       
            cmds.setKeyframe(attribute=self.Attrib, t=(self.St_lin,i), v=self.Va_lin)
            
    def C_UpSlope(self):        
        graph_creater.Post_val()        
        mkP = (self.End_lin + self.St_lin) / self.Point_lin
        
        Operate = 0
     
        for Frame in range(self.St_lin, self.End_lin+1, mkP):    
            cmds.setKeyframe(attribute=self.Attrib, t=(Frame,Frame))            
            for Va in range(0, Operate+(self.Va_lin+1), self.Va_lin):            
                cmds.setKeyframe(attribute=self.Attrib, t=(Frame,Frame), value=Va)
                Operate = Va                       
    
    def C_DownSlope(self):
        
        graph_creater.Post_val()
        mkP = (self.End_lin + self.St_lin) / self.Point_lin        
        Operate = self.Va_lin * self.Point_lin
        
        for Frame in range(self.St_lin, self.End_lin+1, mkP):
            cmds.setKeyframe(attribute=self.Attrib, t=(Frame,Frame))            
            for Va in range(self.Va_lin, Operate+1, self.Va_lin):            
                cmds.setKeyframe(attribute=self.Attrib, t=(Frame,Frame), value=Va)
                Operate = Va - self.Va_lin        
        
    def C_Wave(self):
        graph_creater.Post_val()                       
        mkP = (self.End_lin + self.St_lin) / self.Point_lin
                
        for i in range(self.St_lin, self.End_lin+1, mkP):                        
            cmds.setKeyframe(attribute=self.Attrib, t=(self.St_lin,i), v=0)            
            for Up in range(self.St_lin+mkP, self.End_lin+1, mkP+(mkP*3)):                
                cmds.setKeyframe(attribute=self.Attrib, t=(Up,Up), v=self.Va_lin)                               
                for Down in range(mkP*3, self.End_lin+1, mkP+(mkP*3)):                    
                    cmds.setKeyframe(attribute=self.Attrib, t=(Down,Down), v=0-self.Va_lin)
        
    def C_Bouncing(self):
        graph_creater.Post_val()                       
        mkP = (self.End_lin + self.St_lin) / self.Point_lin
                
        for i in range(self.St_lin, self.End_lin+1, mkP):                        
            cmds.setKeyframe(attribute=self.Attrib, t=(self.St_lin,i), v=0)            
            for Up in range(self.St_lin+mkP, self.End_lin+1, mkP+mkP):                
                cmds.setKeyframe(attribute=self.Attrib, t=(Up,Up), v=self.Va_lin)
    
    def Post_val(self):
        
        Trans = cmds.checkBoxGrp(self.attr, v1=True, q=True)
        Rotat = cmds.checkBoxGrp(self.attr, v2=True, q=True)
        Scale = cmds.checkBoxGrp(self.attr, v3=True, q=True)
        Ax = cmds.checkBoxGrp(self.axle, v1=True, q=True)
        Ay = cmds.checkBoxGrp(self.axle, v2=True, q=True)
        Az = cmds.checkBoxGrp(self.axle, v3=True, q=True)
        self.St_lin = cmds.intFieldGrp(self.St_val, v1=True ,q=True)
        self.End_lin = cmds.intFieldGrp(self.End_val, v1=True ,q=True)
        self.Va_lin = cmds.intFieldGrp(self.Va_val, v1=True ,q=True)
        self.Point_lin = cmds.intFieldGrp(self.Point_val, v1=True ,q=True)
        
        if Trans == True:
           self.attr_val = 'translate'
           #print('translate')           
        elif Rotat == True:
           self.attr_val = 'rotate'           
        elif Scale == True:
           self.attr_val = 'scale'           
        if Ax == True:
           self.axle_val = 'X'           
        elif Ay == True:
           self.axle_val = 'Y'           
        elif Az == True:
           self.axle_val = 'Z'
                      
        self.Attrib = self.attr_val + self.axle_val           
        return self.Attrib, self.St_lin, self.End_lin, self.Va_lin, self.Point_lin

graph_creater = Graph()

cmds.window()
cmds.rowColumnLayout(numberOfColumns=3, cs=[(1,5),(2,5),(3,5)], cw=[(1,150),(2,150),(3,150)], rs=[(1,5),(2,5)])
cmds.button(label='Linear Graph', c='graph_creater.Popup_menu(1)', h=100)  
cmds.button(label='UpSlope Graph', c='graph_creater.Popup_menu(2)')
cmds.button(label='DownSlope Graph', c='graph_creater.Popup_menu(3)')
cmds.button(label='Wave Graph', c='graph_creater.Popup_menu(4)',h=100)
cmds.button(label='Bouncing Graph', c='graph_creater.Popup_menu(5)')
cmds.showWindow()                 

