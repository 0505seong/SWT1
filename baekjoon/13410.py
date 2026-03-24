n, k = map(int, input().split())
max_val = -1 

for i in range(1, k + 1):
    result = n * i
    reversed_str = str(result)[::-1]
    reversed_num = int(reversed_str)
    if reversed_num > max_val:
        max_val = reversed_num

print(max_val)
