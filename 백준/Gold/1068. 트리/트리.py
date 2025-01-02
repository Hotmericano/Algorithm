def dfs(node, tree, deleted):
    deleted.append(node)  # 현재 노드를 방문
    for child in tree[node]:  # 자식 노드들 탐색
        if child not in deleted:
            dfs(child, tree, deleted)

deleted_nodes = []

n = int(input())

parent_node = list(map(int,input().split()))
node_to_delete = int(input())
count = 0
tree = {}

for i in range(n):
    tree[i] = []

for i in range(n):   #트리 구현
    if parent_node[i] != -1:
        tree[parent_node[i]].append(i)
for parent in tree:
    if node_to_delete in tree[parent]:
        tree[parent].remove(node_to_delete)

dfs(node_to_delete, tree, deleted_nodes)

for delete_node in deleted_nodes:
    tree.pop(delete_node, None)

for parent in tree:
    if tree[parent] == []:
        count += 1

print(count)
