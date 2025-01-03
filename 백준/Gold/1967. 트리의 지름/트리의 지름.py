from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
n = int(input())

tree = defaultdict(list)

for i in range(n-1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))   #양방향

def dfs(node, distance):
    visited.add(node)
    global farthest_node, max_distance
    if distance > max_distance:
        max_distance = distance
        farthest_node = node
    for neighbor, weight in tree[node]:
        if neighbor not in visited:
            dfs(neighbor, distance + weight) 


visited = set()
max_distance = 0
farthest_node = 1 #일단 1에서 시작
dfs(1,0)

visited = set()
max_distance = 0
dfs(farthest_node, 0)

print(max_distance)