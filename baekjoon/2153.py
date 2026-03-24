import math
word = input().strip()
total_sum = 0

for char in word:
    if char.islower():
        total_sum += ord(char) - 96
    elif char.isupper():
        total_sum += ord(char) - 38

is_prime = True

if total_sum == 1:
    is_prime = True
else:
    for i in range(2, int(math.sqrt(total_sum)) + 1):
        if total_sum % i == 0:
            is_prime = False
            break

if is_prime:
    print("It is a prime word.")
else:
    print("It is not a prime word.")
