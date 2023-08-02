import os
import maya.cmds as cmds

class build_asset():
    def maya_scene(self, path):
        cmds.file(path, o=True, f=True)
    
    def abc_shade(self, shade_path, model_path, namesp):#ref
        np_lookdev = namesp + '_shade'
        np_model = namesp + '_model'
        def import_file(path):
            file_type = path.split('.')[1]
            if file_type == 'ma':
                cmds.file(path, i=True, ignoreVersion=True, mergeNamespacesOnClash=False, namespace=np_lookdev)
                shading_group = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='{}_lookdevSG'.format(namesp))
                cmds.connectAttr('{}:main_lookdev.outColor'.format(np_lookdev), '{}.surfaceShader'.format(shading_group), f=True)
            elif file_type == 'abc':
                cmds.file(path, i=True, type="Alembic", rnn=True, namespace=np_model)
                   
        import_file(shade_path)       
        import_file(model_path)
        
        cmds.sets('{}:main_model'.format(np_model), e=True, fe='{}_lookdevSG'.format(namesp))
        
class build_shot():
    def abc_shade_anim(self, shade_path, anim_path, namesp):
        np_lookdev = namesp + '_shade'
        np_anim = namesp + '_anim'
        def import_file(path):
            file_type = path.split('.')[1]
            if file_type == 'ma':                
                cmds.file(path, i=True, ignoreVersion=True, mergeNamespacesOnClash=False, namespace=np_lookdev)
                shading_group = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='{}_lookdevSG'.format(namesp))
                cmds.connectAttr('{}:main_lookdev.outColor'.format(np_lookdev), '{}.surfaceShader'.format(shading_group), f=True)
            elif file_type == 'abc':
                cmds.file(path, i=True, type="Alembic", rnn=True, namespace=np_anim)
                   
        import_file(shade_path)       
        import_file(anim_path)
        
        cmds.sets('{}:main_anim'.format(np_anim), e=True, fe='{}_lookdevSG'.format(namesp))
        # cmds.sets('main_anim', e=True, fe='main_lookdevSG')
        
        # file -import -type "mayaAscii"  -ignoreVersion -ra true -mergeNamespacesOnClash false -namespace "TestProject_lookdev_Rex" -options "v=0;"  -pr  -importFrameRate true  -importTimeRange "override" "X:/pipeline/TestProject_lookdev_Rex.ma";
        



