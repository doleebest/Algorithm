# 루트 없는 트리
# 트리의 루트 1
# 노드 개수 n
# 트리 상에서 연결된 두 정점
# 각 노드의 부모를 구해라
import sys
sys.setrecursionlimit(10**6)

n = int(input()) # 노드 개수
tree = [[] for _ in range(n+1)]
for i in range(n-1) :
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a) # 방향성이 없으므로 이렇게 연결되어있음을 보여준다.

visited = [0]*(n+1)
parent = [0] * (n+1)
def dfs(v) : 
    visited[v] = True
    for i in tree[v] :
        if not visited[i] :
            parent[i] = v # 부모 기록
            dfs(i)

dfs(1)

for i in range(2, n+1) :
    print(parent[i])