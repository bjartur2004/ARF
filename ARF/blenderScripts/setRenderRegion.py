import bpy
import sys

argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"

print(argv)  

sc = bpy.data.scenes['Scene']
sc.render.use_border = True

sc.render.border_min_x = 0.5
sc.render.border_max_x = 0.8
sc.render.border_min_y = 0.5
sc.render.border_max_y = 0.8
bpy.ops.wm.save_mainfile()

print("border set uwu")