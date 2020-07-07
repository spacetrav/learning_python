
absolute_path = '/Users/space/OneDrive/Files/Python/rename'

import glob
import os

path = absolute_path
for i, filename in enumerate(glob.glob(path + '*.jpg')):
    os.rename(filename, os.path.join(path, 'captured' + str(i) + '.jpg'))

# def rename(f_path, new_name):
#     filelist = glob2.glob(f_path + "*.jpg")
#     count = 0
#     for file in filelist:
#         print("File Count : ", count)
#         filename = os.path.split(file)
#         print(filename)
#         new_filename = f_path + new_name + str(count + 1) + ".ma"
#         os.rename(f_path+filename[1], new_filename)
#         print(new_filename)
#         count = count + 1

# rename(absolute_path, 'rename_test')