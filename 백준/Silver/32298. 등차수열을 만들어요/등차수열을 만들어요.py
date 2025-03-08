def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def solve(N, M):
    first = 1

    while True:
        sequence = [first + i * M for i in range(N)]
        prime_check = 0

        if max(sequence) > 2000000:
            return [-1]
        
        for num in sequence:
            if (is_prime(num)):
                prime_check = 1
                break
        if (prime_check == 0):
            return sequence
        
        first += 1

N, M = map(int, input().split())
result = solve(N, M)

if result[0] == -1:
    print(-1)
else:
    for num in result:
        print(num, end=" ")