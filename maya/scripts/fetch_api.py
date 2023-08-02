import sys
import json 
import os
# sys.path.append(r"C:\Users\High Tower\AppData\Roaming\Python\Python39\site-packages")
# from shotgun_api3 import Shotgun

_DIR_ = os.path.dirname(__file__)

# sg = Shotgun('https://alejanwong.shotgrid.autodesk.com/', 'test', 'exkn7fpl#vkuukqbgkjhcvQsr')
# sg = Shotgun('https://riff-intern.shotgrid.autodesk.com/', 'filemanager', 'mmuzarqwmxdvvsjin4Uebhtz%')
json_path = r'{}/shotgrid.json'.format(_DIR_)

class fetcher():
    def __init__(self):                
        # self.project_find = sg.find('Project', [['sg_status','is','Active']], ['name'])
        self.json_data = self.read_json(json_path)
        self.project_find = self.json_data["Project"]
           
    def read_json(self, json_path):
        with open(json_path, 'r') as file:
            data = json.load(file)
        return data
        
    def load_all(self):
        
        # self.tasks = sg.find('Task', [['project', 'is', self.project_query]], ['entity', 'content'])
        # self.assets = sg.find('Asset', [['project', 'is', self.project_query]], ['code', 'sg_asset_type'])        
        # self.shots = sg.find('Shot', [['project', 'is', self.project_query]], ['code', 'sg_sequence'])
        self.tasks = self.json_data["Task"]
        self.assets = self.json_data["Asset"]
        self.shots = self.json_data["Shot"]
        
        
              
    def project_list(self):        
        projectList = []
        for proj in self.project_find:
            projectList.append(proj['name'])
        return projectList
    
    def entity_list(self):
        entityList = []
        for entitie in self.assets:
            entityList.append(entitie['code'])
        return entityList
    
    def shot_list(self):
        shotList = []
        for shot in self.shots:
            shotList.append(shot['code'])
        return shotList
        
        
    def get_project(self, project):
        # self.project_query = sg.find_one('Project', [['name', 'is', project]], ['name'])
        self.load_all()
           
    def get_step(self, step):
        self.task_use, self.asset_use, self.shot_use = [],[],[]
        for task in self.tasks:
            if task['content'] == step:
                self.task_use.append(task)#<-----------        
        for asset in self.assets:
            for task_1 in self.task_use:
                if asset['code'] == task_1['entity']['name']:
                    asset['sg_type'] = asset['sg_asset_type']
                    self.asset_use.append(asset)#<-----------
        if self.asset_use == []:
            self.asset_use = [{'type': 'Asset', 'code': 'No file', 'sg_type': 'No root file'}]        
        
        for shot in self.shots:
            for task_2 in self.task_use:
                if shot['code'] == task_2['entity']['name']:
                    shot['sg_type'] = shot['sg_sequence']['name']                    
                    self.shot_use.append(shot)#<-----------
        if self.shot_use == []:
            self.shot_use = [{'type': 'Shot', 'code': 'No file', 'sg_type': 'No root file'}]         
        
        #-------------------------------------------------------
        # output self.task_use, self.asset_use, self.shot_use  
        #-------------------------------------------------------
        
    def transform(self):
        use_list = self.asset_use + self.shot_use
        transform_dict = {}

        for item in use_list:
            asset_type = item['type']
            code = item['code']
            sg_type = item['sg_type']

            if asset_type not in transform_dict:
                transform_dict[asset_type] = {}

            if sg_type not in transform_dict[asset_type]:
                transform_dict[asset_type][sg_type] = set()

            transform_dict[asset_type][sg_type].add(code)

        return transform_dict
        
    
    def merge_data(self):   
        
        use_list = self.asset_use + self.shot_use
        
        return use_list
    
    def shot_data(self):
        
        return self.shots
    
    def asset_data(self):
        
        return self.assets

    
    

    
        
            
            
            


