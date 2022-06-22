import mat73
import h5py
import numpy as np
with h5py.File('CyTOFData.mat', 'r') as f:
    print(f.keys())
    
arrays = {}
for k, v in f.items():
    print(k)
    print(v)
    arrays[k] = np.array(v)
# data_dict = mat73.loadmat("CyTOFData.mat")
# print(len(data_dict))