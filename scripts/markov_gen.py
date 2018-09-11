# OUTNAME : name of .h5 file that is out
# TICA_IN : input tica file
# Saves and generates markov models

def markov_generator(outname, tica_in):
    
    start = time.time()

    Y = np.load(str(tica_in))
    
    # Kmeans Clustering
    cl = coor.cluster_kmeans(data=Y, k=50, stride=1, max_iter=50)
    cl.save(str('./markov_gen_out/' + outname + '.h5'), 'cluster')
    
    print('\nKMEANS SAVED; SAVING DTRAJ\n')
    
    # Extracting coordinate data
    dtrajs = cl.dtrajs
    cl.save_dtrajs(trajfiles=['./markov_gen_out/' + outname], output_dir='./markov_gen_out/')
    
    print('\nFINISHED SAVING DTRAJ; STARTING HMM RUNS\n')
    
    lag = [100, 125, 150, 175]
    
    for i in lag:
        m = msms.estimate_hidden_markov_model(dtrajs, 10, i)
        m.save(str('./markov_gen_out/' + outname + '.h5'), 'lag' + str(i))
        print('\nHMM' + str(i) + 'COMPLETE\n')
    
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
    markov_generator(sys.argv[1], sys.argv[2]) 
