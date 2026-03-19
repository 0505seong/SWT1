h, m, s = map(int, input().split())
more = int(input())

total = h * 3600 + m * 60 + s
total += more
total %= 24 * 3600

h = total // 3600
m = (total % 3600) // 60
s = total % 60

print(h, m, s)
