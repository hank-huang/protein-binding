import pyemma as pe
import pyemma.coordinates as coor
import numpy as np
import pandas as pd

topfile = '/data/ggerlach/encounter_complex/seg1_simualtions1/total1_setup.pdb'
trajfile = ('./seg1_1/analysis/complete_all.nc')

feat = coor.featurizer(topfile)
feat.add_backbone_torsions()
feat.add_distances_ca()

inp = coor.source(trajfile, feat)

tica_obj = coor.tica(inp, lag=5000, dim=2, kinetic_map = True)
    
tica_obj.save(file_name='tica_projections.h5', model_name = 'backbone/ca_distance', overwrite=False)
