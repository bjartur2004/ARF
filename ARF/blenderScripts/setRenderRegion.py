import bpy
import sys

argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"

print(argv)  

sc = bpy.data.scenes['Scene']
sc.render.use_border = True

sc.render.border_min_x = float(argv[0])
sc.render.border_max_x = float(argv[1])
sc.render.border_min_y = float(argv[2])
sc.render.border_max_y = float(argv[3])
bpy.ops.wm.save_mainfile()

print("border set")
