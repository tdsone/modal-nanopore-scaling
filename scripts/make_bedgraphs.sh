bedtools genomecov -split -bg -strand + \
        -i /Users/tds122/Documents/phd/modal-nanopore-scaling/alignment_JS610_20190307_porechopped_filtered_canuCorrected_distinguished.bed -g /Users/tds122/Documents/phd/modal-nanopore-scaling/JS610.noERCC.sizes > JS610.plus.bedGraph
bedtools genomecov -split -bg -strand - \
        -i /Users/tds122/Documents/phd/modal-nanopore-scaling/alignment_JS610_20190307_porechopped_filtered_canuCorrected_distinguished.bed -g /Users/tds122/Documents/phd/modal-nanopore-scaling/JS610.noERCC.sizes > JS610.minus.bedGraph