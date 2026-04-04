N = int(input())
number = []

for i in range(N):
    num = int(input())
    number.append(num)
    
number.sort()

for n in number:
    print(n)
