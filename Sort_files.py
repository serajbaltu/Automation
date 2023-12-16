import os
import shutil

path = os.getcwd()

for filename in os.listdir(path):
    if os.path.isfile(os.path.join(path, filename)):
        folder_name = os.path.splitext(filename)[1][1:]
        if not os.path.exists(os.path.join(path, folder_name)):
            os.makedirs(os.path.join(path, folder_name))
        shutil.move(os.path.join(path, filename), os.path.join(path, folder_name, filename))