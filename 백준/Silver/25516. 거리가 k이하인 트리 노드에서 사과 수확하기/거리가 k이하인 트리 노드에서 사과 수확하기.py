import sys
sys.setrecursionlimit(10**6)

def dfs(node, distance):
    global count
    visited[node] = True
    if distance <= K and has_apple[node]:
        count += 1
    for neighbor in tree[node]:
        if not visited[neighbor]:
            dfs(neighbor, distance+1)

N, K = map(int, input().split())

tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)

has_apple = list(map(int, input().split()))

visited = [False] * (N + 1)
count = 0
dfs(0, 0)
print(count)
