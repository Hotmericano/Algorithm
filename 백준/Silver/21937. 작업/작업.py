from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

graph = defaultdict(list)

def DFS(start, visited=set()): 
    visited.add(start)
    for node in graph[start]:
        if node not in visited:
            DFS(node, visited)
    return visited


n,m = map(int, input().split())

for i in range(m):
    start, end = map(int, input().split())
    graph[end].append(start)

target = int(input())
print(len(DFS(target))-1)