n = int(input())
member = []

for i in range(n):
    age, name = input().split() 
    member.append([int(age),name])

member.sort(key=lambda member: member[0])


for i in range(n):
    print(f"{member[i][0]} {member[i][1]}")