from PIL import Image
import os

ratioNeeded = 16/9;

for f in os.listdir():
  if ('jpg' in f) or ('png' in f) or ('jpeg' in f):
    width, height = (1,1)
    with Image.open(f) as img:
      width, height = img.size
    if (width/height == ratioNeeded):
      print('Accepted!')
    else:
      os.remove(f)

