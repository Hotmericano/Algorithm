n =  int(input())
ef_table = [0 for i in range(n)]
ef_power = list(map(int, input().split()))

ef_power = list(reversed(sorted(ef_power)))

for i in range(n):
    for j in range(ef_power[i]):
        ef_table[(i+j+1)%n] = 1
        
print(ef_table.count(1))
