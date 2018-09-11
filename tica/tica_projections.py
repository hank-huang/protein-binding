import pyemma
import pyemma.coordinates as coor
import numpy as np

topfile = '/data/ggerlach/encounter_complex/seg1_simualtions1/total1_setup.pdb'
trajfile = '/data/hhuang/ArkA_S1_MSM/seg1_1/analysis/complete_all.nc'

###################################
## Backbone Torsion              ##
## alpha-Carbon Distance         ##
###################################

feat = coor.featurizer(topfile)
feat.add_backbone_torsions()
feat.add_distances_ca()

inp = coor.source(trajfile, feat)

# Lagtime 2000 steps

feat_tica_obj = coor.tica(inp, lag = 2000, dim = 2, kinetic_map = True)

# Save object to csv
feat_tica_obj.write_to_csv('backbone_torsion//ca_distances', extension = '.dat')

