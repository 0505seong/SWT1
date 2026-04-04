import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
x.sort()

total_distance = 0

for i in range(n):
    total_distance += x[i] * (2 * i - 2 * (n - 1 - i))

print(total_distance)
