import argparse
import nbformat

parser = argparse.ArgumentParser(description='Parse jupyter notebooks to remove cells programmatically')
parser.add_argument('infile', type=str, nargs=1, help='name of notebook file to parse')
parser.add_argument('outfile', type=str, nargs=1, help='name to write output file as')
parser.add_argument('--magic-comment', type=str, default="okpy_solution")

args = parser.parse_args()
assert(len(args.infile) == 1)
assert(len(args.outfile) == 1)

infile = args.infile[0]
outfile = args.outfile[0]

nbversion = 4

nb = nbformat.read(fp=infile, as_version=nbversion)

magic_comment = "nbstrip"

newnb = nbformat.v4.new_notebook()
newnb.cells = [x for x in nb.cells if not (x.cell_type == "code" and (x.source.startswith("# " + magic_comment) or x.source.startswith("#" + magic_comment)))]
nbformat.write(newnb, outfile)
