import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('PatientMetaData.csv')
processed = data.drop_duplicates('PID')
processed.to_csv('ProcessedMetaData.csv',index=False)
print("og:",data.shape)
print("nodupes:", processed.shape)
train, test = train_test_split(processed, test_size=0.2)
print("train:",train.shape)
print("test",test.shape)
train.to_csv("train_data.csv",index=False)
test.to_csv("test_data.csv",index=False)