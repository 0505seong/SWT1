numbers = []
num_42 = []

for i in range(10):
    c = int(input())
    numbers.append(c)
    
for num in numbers:
    a= num % 42
    num_42.append(a)
    
b = len(set(num_42))
print(b)
