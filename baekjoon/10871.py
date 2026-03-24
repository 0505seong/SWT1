n, x = map(int, input().split())
a = list(map(int, input().split()))
result = [str(i) for i in a if i < x]

print(" ".join(result))
