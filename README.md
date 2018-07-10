# nbparse
Parse Jupyter notebooks to remove tagged cells

Quickstart:

```
python nbparse.py <infile> <outfile> --magic_comment [okpy_solution]
```

where:

`infile`: a jupyter notebook that has some code cells tagged by starting
with a "magic comment", specified as an option.

`outfile`: name of output file where `nbparse` will write a jupyter
notebook that has the tagged cells removed.

`magic_comment` [default: `okpy_solution`]: The comment (without the
`#`) that marks a cell to be removed in the output
