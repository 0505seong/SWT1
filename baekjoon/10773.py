numbers = []
N = int(input())

for i in range(N):
    a = int(input())
    
    if a == 0:
        numbers.pop()
    else:
        numbers.append(a)
        
print(sum(numbers))
