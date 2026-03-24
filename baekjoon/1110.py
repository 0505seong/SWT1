n = int(input())
original_n = n  
count = 0       

while True:
    tens = n // 10
    ones = n % 10
    total = tens + ones
    n = (ones * 10) + (total % 10)
    count += 1
    
    if n == original_n:
        break

print(count)
