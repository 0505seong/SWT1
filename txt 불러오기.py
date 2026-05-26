import os

path = input()

file_list = os.listdir(path)
txtFiles = []

for files in file_list:
    if files[-4:] == '.txt':
        txtFiles.append(files)

print(txtFiles)