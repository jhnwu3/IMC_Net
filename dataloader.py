import os
import numpy as np
import torch as tc
import pandas as pd
import cv2
from torchvision import transforms
from PIL import Image
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split

# Goal #1: Be able to read patient meta data 
# Goal #2: Be able to match patient meta data to a respective directory
# Goal #3: Load 1 (pid) of pngs into a torch tensor
# Goal #4: Load all of pngs into torch tensors 
# Goal #5: Break up dataset into 1 train, 1 test
# dataset directory: tiff_data/pidxxx/xx.png
class IMCDataset(Dataset):
    """Face Landmarks dataset."""

    def __init__(self, csv_file, root_dir, transform=None):
        """
        Args:
            csv_file (string): Path to the csv file with annotations.
            root_dir (string): Directory with all the images.
            transform (callable, optional): Optional transform to be applied
                on a sample.
        """
        self.imc_frame = pd.read_csv(csv_file) # PatientMetaData.csv
        self.root_dir = root_dir # i.e something like test_data
        self.transform = transform

    def __len__(self):
        return len(self.imc_frame)

    def __getitem__(self, idx):
        if tc.is_tensor(idx):
            idx = idx.tolist()

        images_dir = os.path.join(self.root_dir,
                                "pid" +self.imc_frame["pid"])
        
        
        listOfImages = os.listdir(images_dir)
        image = Image.open(dir + "/" + listOfImages[idx]) # process all 42 images into one thing???
        label = self.imc_frame

        if self.transform:
            sample = self.transform(sample)

        return sample
    
    
# Goal #1
data = pd.read_csv('train_data.csv')

# for fun: Get average tumor size of patients that died in general.

# aliveSizes = []
# deadSizes = []
# for i in range(data.shape[0]):
#     if(data["Patientstatus"][i] == "alive" or data["Patientstatus"][i] =="alive w metastases"):
#         aliveSizes.append(data["tumor_size"][i])
#     else:
#         deadSizes.append(data["tumor_size"][i]) 
         
# aliveSizes = np.array(aliveSizes)
# deadSizes = np.array(deadSizes)
# print("tumor size average alive:", np.average(aliveSizes))
# print("tumor size average death", np.average(deadSizes))
# print(data["Patientstatus"][4])
# print(dir)
# Goal #2: Be able to match patient meta data to a respective directory

dir = "tiff_data/pid" + str(data["PID"][0])
print(data["PID"].shape)
# Goal #3: Load 1 (pid) of pngs into a torch tensor
listOfImages = os.listdir(dir)
img = Image.open(dir + "/" + listOfImages[0])
img.resize()
convert_tensor = transforms.ToTensor()
tensor = convert_tensor(img)
print(tensor.shape)
# Goal #4: Load all of pngs into torch tensors )