import sys

b = sys.stdin.readline().strip()

if len(b) % 3 == 1:
    b = '00' + b
elif len(b) % 3 == 2:
    b = '0' + b

res = "".join(str(int(b[i:i+3], 2)) for i in range(0, len(b), 3))

print(res)
