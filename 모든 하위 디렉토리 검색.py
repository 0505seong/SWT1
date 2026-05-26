import os
base = input()
def listAll(path):
    dirfiles = os.listdir(path)
    subdirs = [path + "/" + x for x in dirfiles if os.path.isdir(path + "/" +
x)]
    print(path)
    for subdir in subdirs:
        listAll(subdir)

listAll(base)