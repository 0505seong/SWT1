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

def multiply(A, B):
    result = []
    for i in range(n):
        result.append([])
        for j in range(n):
            total = 0
            for k in range(n):
                total += A[i][k] * B[k][j]
            result[i].append(total)
    return result

def add(A, B):
    result = []
    for i in range(n):
        result.append([])
        for j in range(n):
            result[i].append(A[i][j] + B[i][j])
    return result

def printing_result(metrix):
    for i in range(n):
        for j in range(n):
            print(f'{metrix[i][j]:6d}', end=' ')
        print()

print('a')
a = printing_matrix()
print('\nb')
b = printing_matrix()
print('\nc')
c = printing_matrix()

print('\nA x B + C]')
printing_result(add(multiply(a, b), c))