# OUTNAME : Name of the .h5 file that is output
# TICA_IN : TICA data to be read in
# STATES : list of states to run tica in 

def coorcluster(outname, tica_in, states):
    
    # For timing purposes
    start = time.time()
    
    # Loading in TICA
    Y = np.load(str(tica_in))
        
    # Loop to ensure that multiple cluster numbers can be run
    for i in states:
        # Saving k_means coordinate object
        cl = coor.cluster_kmeans(data=Y, k=i, stride=1, max_iter=500)
        cl.save(str('./markov_gen_out/' + outname + '.h5'), 'cluster' + str(i))
        
        # Saving trajectory seperately as a list
        dtrajs = cl.dtrajs
        np.save('./markov_gen_out/' + outname + str(i) + '__NPARR', dtrajs)
        cl.save_dtrajs(trajfiles=['./markov_gen_out/' + outname + str(i)], output_dir='./markov_gen_out/')       
        
        sys.stderr.write('\n######PROJECT_DONE########: ' + str(i) + '\n')
    
    end = time.time()
    
    sys.stderr.write('\n######TIME_ECLIPSED########: ' + str(end - start) + '\n')
    
    
if __name__ =='__main__':
    import os
    import pyemma as pe
    import time
    from glob import glob
    import pyemma.msm as msm
    import pyemma.coordinates as coor
    import sys
    import numpy as np
    import matplotlib.pyplot as plt
    plt.switch_backend('agg')
    coorcluster(sys.argv[1], sys.argv[2]) 
