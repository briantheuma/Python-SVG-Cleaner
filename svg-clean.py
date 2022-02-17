import os
import re
import shutil

cwd = os.getcwd()
svg_folder = f"{cwd}/01-original-svgs/"
svg_output_folder = f"{cwd}/02-cleaned-svgs/"

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

copytree(svg_folder, svg_output_folder)

for dname, dirs, files in os.walk(svg_output_folder):
    for fname in files:
        fpath = os.path.join(dname, fname)
        with open(fpath, 'rb') as f:
            data = f.read().decode(errors='replace')
            data = re.sub(r'fill-rule=".*?"', '', data)
            data = re.sub(r'<title>.*?</title>', '', data)
            data = re.sub(r'<g .*?>', '', data)
            data = re.sub(r'<g .*?>', '', data)
            data = re.sub(r' id=".*?"', '', data)
            data = re.sub(r'fill=".*?"', '', data)
            data = data.replace('<g>', '')
            data = data.replace('</g>', '')
            data = data.replace('<?xml version="1.0" encoding="UTF-8"?>', '')
            data = data.replace('\n', '')

        with open(fpath, "w") as f:
            f.write(data)