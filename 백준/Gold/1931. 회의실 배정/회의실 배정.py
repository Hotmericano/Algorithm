import sys
input = sys.stdin.readline

N = int(input())
table = []

for i in range(N):
    time = list(map(int, input().split()))
    table.append(time)
table.sort(key=lambda x : (x[1],x[0]))
# for i in range(N - 1, 0, -1):
#         for j in range(i):
#             if table[j][1] > table[j + 1][1]:
#                 table[j], table[j + 1] = table[j + 1], table[j]

end = table[0][1]
start = 0
count = 1
for i in range(1,N):
    if table[i][0] >= end:
        count+=1
        end = table[i][1]
print(count)
    
