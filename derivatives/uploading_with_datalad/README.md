# Uploading with DataLad

A new DataLad dataset was created for the conversion, following the README from https://github.com/con/vandermeerlab-to-bids.

Several additional bugs were uncovered and fixed regarding the CLI.

The main annoyance here was how I had to rebuild the container each time I wanted to test a fix, since I was locked into use the `containres-run`.

Next time I will debug more without containers until satisfied.

The datalad config has to be modified to bind the current working directory as well as the symlinked directories which existed on a different mount point.

The `git log` was dumped after the processed data was converted, and can be found adjacent to this README.
