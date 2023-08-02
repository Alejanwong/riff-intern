import maya.cmds as cmds

def import_lookdev_maya_ascii(maya_ascii_file):
    # Check if the file exists
    if not cmds.file(maya_ascii_file, q=True, exists=True):
        raise RuntimeError("The specified Maya ASCII file does not exist: {}".format(maya_ascii_file))

    # Import the Maya ASCII file without creating a new scene
    cmds.file(maya_ascii_file, i=True, ignoreVersion=True, mergeNamespacesOnClash=False, namespace="namespace")

def import_alembic_file(alembic_file):
    # Check if the file exists
    if not cmds.file(alembic_file, q=True, exists=True):
        raise RuntimeError("The specified Alembic file does not exist: {}".format(alembic_file))

    # Import the Alembic file in the current scene
    cmds.AbcImport(alembic_file)

if __name__ == "__main__":
    # Specify the paths to your Maya ASCII file and Alembic file
    maya_ascii_file = r"X:\pipeline\TestProject\Asset\Character\Woody\version_01\lookdev\TestProject_lookdev_Woody.ma"
    alembic_file = r"X:\pipeline\TestProject\Asset\Character\Woody\version_01\anim\TestProject_anim_Woody.abc"

    try:
        # Import the Maya ASCII file without creating a new scene
        import_lookdev_maya_ascii(maya_ascii_file)

        # Import the Alembic file in the same scene
        import_alembic_file(alembic_file)

        print("Import successful!")
    except RuntimeError as e:
        print("Error: {}".format(str(e)))

