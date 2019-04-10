import bpy
import os

files = []  #List of files names in the following format ["C:\\Users\\User\\Downloads\\file1.fbx", "C:\\Users\\User\\Downloads\\file2.fbx"]
for file in files: #For each file
	bpy.ops.object.select_all(action='SELECT') # Select all in scene
	bpy.ops.object.delete() # Clear scene
	bpy.ops.import_scene.fbx(filepath=file) # Change to the type of file being imported
	bpy.ops.object.select_all(action='SELECT')
	bpy.ops.wm.collada_export(filepath=os.path.splitext(file)[0] + ".dae") # Change to the type of file being exported
