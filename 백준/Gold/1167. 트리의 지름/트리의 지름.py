from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)
v = int(input())

tree = defaultdict(list)

#트리 구햔(양방향 이동 가능하도록)
for i in range(v):
    inf  = input()
    temp = list(map(int, inf.split(' ')))
    parent = temp[0]
    for i in range(1,len(temp),2):
        if (temp[i] == -1):
            break
        tree[parent].append((temp[i],temp[i+1]))

#dfs 2번으로 트링 지름 구하기

def dfs(node, distance):
    global farthest_node, max_distance
    visited.add(node)

    if distance > max_distance:
        max_distance = distance
        farthest_node = node
    
    for neighbor, weight in tree[node]:
        if neighbor not in visited:
            dfs(neighbor, weight + distance)

visited = set()
max_distance = 0
farthest_node = 1
dfs(1, 0)

visited = set()
max_distance = 0
dfs(farthest_node, 0)

print(max_distance)