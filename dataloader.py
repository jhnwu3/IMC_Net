import mat73
import h5py
with h5py.File('CyTOFData.mat', 'r') as f:
    print(f.keys())
# data_dict = mat73.loadmat("CyTOFData.mat")
# print(len(data_dict))