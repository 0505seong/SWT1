import os


path = input()

with os.scandir(path) as entries:
    for entry in entries:
        print(f"이름: {entry.name}, 경로: {entry.path}")