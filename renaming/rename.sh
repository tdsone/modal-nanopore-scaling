# bw to bg
bigWigToBedGraph /Users/tds122/Documents/phd/modal-nanopore-scaling/renaming/minus/JS610.minus.bw /Users/tds122/Documents/phd/modal-nanopore-scaling/renaming/minus/JS610.minus.bg

# rename chroms in bg
python rename.py /Users/tds122/Documents/phd/modal-nanopore-scaling/renaming/minus/JS610.minus.bg alias.json /Users/tds122/Documents/phd/modal-nanopore-scaling/renaming/minus/JS610.minus.renamed.bg

# turn back into bw
