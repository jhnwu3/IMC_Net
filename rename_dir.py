import os
import re
from pathlib import Path
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
    newName = "pid" + newName[4:]
    my_file = Path(newName)
    samePID = 1
    while my_file.exists():
      newName = str(samePID) + newName
      my_file = Path(newName)
      samePID+=1
    os.rename(fn ,newName)
  
#   if ',' in fn:
#     continue # Already in the correct form
#   if ' ' not in fn:
#     continue # Invalid format
#   firstname,_,surname = fn.rpartition(' ')
#   os.rename(os.path.join(basedir, fn),
#             os.path.join(basedir, surname + ', ' + firstname))