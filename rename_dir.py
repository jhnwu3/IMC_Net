import os
import re
def findID(gate):
  return re.findall("_000[0-9]*", gate)


ogName = 'png'
nImgs = 381
imgDirs = []
for i in range(nImgs):
    imgDirs.append(ogName + str(i+1))
    
with open('img_gates.csv') as file:
  gates = file.readlines()
  gates = [line.rstrip() for line in gates]
gates = gates
    
basedir = './'
# print(imgDirs)
# print(os.listdir(basedir))
# print(newListOfNames)
for fn in os.listdir(basedir):
  if not os.path.isdir(os.path.join(basedir, fn)):
    continue # Not a directory
  if fn in imgDirs:
    newName = gates[imgDirs.index(fn)]
    newName = findID(newName)[0]
    print("pid" + newName[4:])
  
#   if ',' in fn:
#     continue # Already in the correct form
#   if ' ' not in fn:
#     continue # Invalid format
#   firstname,_,surname = fn.rpartition(' ')
#   os.rename(os.path.join(basedir, fn),
#             os.path.join(basedir, surname + ', ' + firstname))