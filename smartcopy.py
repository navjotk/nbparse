import argparse
import os
import shutil
from nbparse import nbparse


parser = argparse.ArgumentParser(description='Parse jupyter notebooks to remove cells programmatically')
parser.add_argument('indir', type=str, nargs=1, help='name of notebook file to parse')
parser.add_argument('outdir', type=str, nargs=1, help='name to write output file as')

args = parser.parse_args()

indir = args.indir[0]
outdir = args.outdir[0]

pathsep = "/"

# Create output directory if does not exist already
if not os.path.isdir(outdir):
    os.makedirs(outdir)

# Walk through every file in indir
for fullname in os.listdir(indir):
    filename, file_extension = os.path.splitext(fullname)

    if file_extension == ".ipynb":
        nbparse(indir + pathsep + fullname, outdir + pathsep + fullname, magic_comment="OKPY_SOLUTION")
    else:
        if os.path.isdir(indir + pathsep + fullname):
            shutil.copytree(indir + pathsep + fullname, outdir + pathsep + fullname)
        else:
            shutil.copyfile(indir + pathsep + fullname, outdir + pathsep + fullname)
        

