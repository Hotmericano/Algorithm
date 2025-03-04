n =  int(input())

ef_power = list(map(int, input().split()))

ef_power = list(reversed(sorted(ef_power)))
answer = 0
for i in range(n):
    if ef_power[i] == 0:
        break
    answer = max(answer, i+ef_power[i]) # i+인 이유: 전거는 무조건 강화되어 있음

print(min(n,answer))
