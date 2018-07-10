import argparse
import nbformat


def nbparse(infile, outfile, magic_comment="nbstrip"):
    print("Removing comment %s" % magic_comment)
    nbversion = 4
    nb = nbformat.read(fp=infile, as_version=nbversion)
    oldcells = len(nb.cells)
    newnb = nbformat.v4.new_notebook()
    newnb.cells = [x for x in nb.cells if not (x.cell_type == "code" and (x.source.startswith("# " + magic_comment) or x.source.startswith("#" + magic_comment)))]
    newcells = len(newnb.cells)
    print("%d cells removed" % (oldcells - newcells))
    nbformat.write(newnb, outfile)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse jupyter notebooks to remove cells programmatically')
    parser.add_argument('infile', type=str, nargs=1, help='name of notebook file to parse')
    parser.add_argument('outfile', type=str, nargs=1, help='name to write output file as')
    parser.add_argument('--magic-comment', type=str, default="okpy_solution")

    args = parser.parse_args()
    assert(len(args.infile) == 1)
    assert(len(args.outfile) == 1)

    infile = args.infile[0]
    outfile = args.outfile[0]
    nbparse(infile, outfile, magic_comment = args.magic_comment)
