import sys
input = sys.stdin.readline
H,Q = map(int, input().split())
square = []

for i in range(H):
    column = list(map(int, input().split()))
    square.append(column)

sum = [[0 for _ in range(H+1)] for _ in range(H+1)]

for i in range(1,H+1):
    for j in range(1,H+1):
        sum[i][j] = sum[i][j-1] + square[i-1][j-1]

for i in range(1,H+1):
    for j in range(1, H+1):
        sum[j][i] = sum[j-1][i] + sum[j][i]

for i in range(Q):
    l,r,L,R = map(int, input().split())
    print(sum[L][R] + sum[l-1][r-1] - sum[l-1][R] - sum[L][r-1])