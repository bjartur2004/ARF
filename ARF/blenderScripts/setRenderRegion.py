import bpy
import sys

#argv = sys.argv
#argv = argv[argv.index("--") + 1:]  


#bpy.data.scenes['Scene'].render.border_min_x = float(argv[0])
#bpy.data.scenes['Scene'].render.border_max_x = float(argv[1])
#bpy.data.scenes['Scene'].render.border_min_y = float(argv[2])
#bpy.data.scenes['Scene'].render.border_max_y = float(argv[3])

bpy.data.scenes['Scene'].render.border_min_x = 0
bpy.data.scenes['Scene'].render.border_max_x = 0.5
bpy.data.scenes['Scene'].render.border_min_y = 0
bpy.data.scenes['Scene'].render.border_max_y = 0.5