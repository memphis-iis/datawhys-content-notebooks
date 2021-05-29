import os
import nbformat as nbf

for file in os.listdir('.'):
    if file.endswith('.ipynb'):
        ntbk = nbf.read(file, nbf.NO_CONVERT)
        cells_to_keep = []
        for cell in ntbk.cells:
            # we assume that code cells containing serialize blocks are precisely those with solutions we need to delete 
            if cell.cell_type == "code" and "#<xml" in cell.source:
                cell.source = []
            cells_to_keep.append(cell)
        new_ntbk = ntbk
        new_ntbk.cells = cells_to_keep
        nbf.write(new_ntbk, os.path.splitext(file)[0]+'-Exercise.ipynb', version=nbf.NO_CONVERT)
