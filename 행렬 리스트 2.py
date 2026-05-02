import random

n = int(input())

def make_maetrix(row, col):
    metrix = []
    for i in range(row):
        metrix.append([])
        for j in range(col):
            metrix[i].append(random.randint(1, n * n * 10))
    return metrix, row, col

def printing_matrix():
    global n
    metrix, row, col = make_maetrix(n, n)
    for i in range(row):
        for j in range(col):
            print(f'{metrix[i][j]:3d}', end=' ')
        print()
    return metrix

a = printing_matrix()
a_jeon = list(map(list,zip(*a)))

print('\na의 전치행렬')
for i in range(n):
    for j in range(n):
        print(f'{a_jeon[i][j]:3d}', end=' ')
    print()