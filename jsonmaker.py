import glob
import os
from natsort import natsorted
from random import sample 
from random import shuffle


root = "screws/dataset"

root_2 = "counting/dataset"

part_A_train = os.path.join(root,"test","new_images")
part_B_train = os.path.join(root_2,"test","new_images")

img_paths_A = natsorted(glob.glob(os.path.join(part_A_train, "*.jpg")))
img_paths_A = sample(img_paths_A,200)

img_paths_B = natsorted(glob.glob(os.path.join(part_B_train, "*.jpg")))
img_paths_B = sample(img_paths_B,200)

print(len(img_paths_B), len(img_paths_A))

img_paths_A.extend(img_paths_B)
print(len(img_paths_A))

shuffle(img_paths_A)
with open('test_combined.json', 'w+') as f:
	f.write('[')
	for i in img_paths_A:
		f.write('"' + i + '",\n')
	f.write(']')
