import mat73
import h5py
import numpy as np
with h5py.File('CyTOFData.mat', 'r') as f:
    print(f.keys())
    
arrays = {}
for k in f.keys():
    print(k)
    f[]
    # print(f[k])
    # arrays[k] = np.array(f[k])
# data_dict = mat73.loadmat("CyTOFData.mat")
# print(len(data_dict))