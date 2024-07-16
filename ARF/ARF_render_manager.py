import subprocess
import sys
import yaml
import os

CONFIG = yaml.safe_load(open("ARF/render_config.yaml"))

# "C:/Program Files/Blender Foundation/Blender 4.0/blender.exe" -b ./renderTest/susans.blend -x 1 -o -f 1

process = subprocess.Popen(
    [CONFIG["setup"]["blender_exe_path"], "-b", "../renderTest/susans.blend", "-x", "1", "-o", "//render" ,"-f", "1"]
    , stdout=subprocess.PIPE, stderr=subprocess.STDOUT
)
for line in process.stdout:
    line = line.decode("utf-8")
    if CONFIG["logging"]["level"] == "ERROR":
        if line[0:5].upper() == "ERROR":
            sys.stdout.write(line)
    else:
        sys.stdout.write(line)

