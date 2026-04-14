M = int(input())
N = int(input())

def prime(start, end):
    is_prime = [True] * (end + 1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(end**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, end + 1, i):
                is_prime[j] = False

    result = []
    for i in range(max(2, start), end + 1):
        if is_prime[i]:
            result.append(i)
    return result

prime_number = prime(M,N)

if len(prime_number) == 0:
    print(-1)
    
else:
    print(sum(prime_number))
    print(min(prime_number))
