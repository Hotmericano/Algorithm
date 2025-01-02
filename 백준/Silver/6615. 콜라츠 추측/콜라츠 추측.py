def collatz(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    sequence.append(1)
    return sequence

def find_common_ancestor(a,b):
    seq_a = collatz(a)
    seq_b = collatz(b)

    set_b = set(seq_b)

    for num in seq_a:
        if num in set_b:
            return num

while True:
    a,b = map(int, input().split())
    if (a == 0 & b == 0):
        break
    result = find_common_ancestor(a,b)
    print(f"{a} needs {collatz(a).index(result)} steps, {b} needs {collatz(b).index(result)} steps, they meet at {result}")
    


