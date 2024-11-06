import sys
input = sys.stdin.readline

n, k = map(int, input().split())

tem = 1
for i in range(k):
    tem *= n
    n -= 1

divisor = 1
for i in range(2, k+1):
    divisor *= i

print((tem // divisor) % 10007)