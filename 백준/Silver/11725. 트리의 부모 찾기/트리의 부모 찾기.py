from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


n = int(input())
graph = defaultdict(list)

for i in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

check = [0] *(n)

def DFS(start):
    for i in graph[start]:
        if check[i-1] == 0:
            check[i-1] = start
            DFS(i)
DFS(1)

for i in range(1,n):
    print(check[i])