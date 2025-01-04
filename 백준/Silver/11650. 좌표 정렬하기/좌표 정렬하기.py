n = int(input())
coordinate = []
for i in range(n):
    coordinate.append(list(map(int,input().split())))

coordinate.sort(key=lambda coordinate: (coordinate[0],coordinate[1]))


for i in range(n):
    print(coordinate[i][0], coordinate[i][1])