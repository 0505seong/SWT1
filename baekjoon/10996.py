n = int(input())

if n == 1:
    print('*')
else:
    for _ in range(n):
        print('* ' * ((n + 1) // 2))
        print(' *' * (n // 2))
