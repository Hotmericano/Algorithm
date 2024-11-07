from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)
graph = defaultdict(set)
input = sys.stdin.readline
n, m = map(int, input().split())

for i in range(m):
    a,b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

visited = set()
def DFS(start):
    visited.add(start)
    for i in graph[start]:
        if i not in visited:
            DFS(i)
    return visited

count = 0;
for i in range(1,n+1):
    if i not in visited:
        DFS(i)
        count += 1
print(count)

