arr = list(range(1,10001))

for i in range(1,10001):
    for j in str(i):
        i+=int(j)
    if i in arr:
        arr.remove(i)

for i in arr:
    print(i)
