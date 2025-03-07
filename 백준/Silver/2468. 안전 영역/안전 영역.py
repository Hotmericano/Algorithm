import sys
sys.setrecursionlimit(100000) 

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, height):
    visited[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and zone[nx][ny] > height:
                dfs(nx, ny, height)

N = int(input())
zone = []
max_height = 0

for i in range(N):
    row = list(map(int, input().split()))
    max_height = max(max_height, max(row))
    zone.append(row)

max_safe_zone = 1 

for height in range(1, max_height):
    visited = [[False] * N for i in range(N)]
    safe_zone = 0
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and zone[i][j] > height:
                dfs(i, j, height)
                safe_zone += 1
    
    max_safe_zone = max(max_safe_zone, safe_zone)

print(max_safe_zone)