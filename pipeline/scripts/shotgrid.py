from shotgun_api3 import Shotgun

sg = Shotgun('https://riff-intern.shotgrid.autodesk.com/', 'filemanager', 'mmuzarqwmxdvvsjin4Uebhtz%')
# project_find = sg.find('Project', [['name','is','TestProject']], ['name'])
project_find = sg.find('Project', [['name','is','TestProject']], ['name'])
shots = sg.find('Task', [['project', 'is', project_find]], ['entity', 'content'])

print(shots)