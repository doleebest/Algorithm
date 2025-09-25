import sys
sys.setrecursionlimit(10**6)

def dfs(node) :
    global ans
    for i in graph[node] :
        if visited[i] == 0:
            visited[i] = -visited[node] # 다른 색으로 색칠
            dfs(i)
        elif visited[i] !=0:
            if visited[i] == visited[node] :
                ans = "NO"
                return # 조기 종료

K = int(sys.stdin.readline())
for _ in range(K) : 
    V,E = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    visited= [0]*(V+1)
    ans = "YES"
    for i in range(E) :
        a,b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for j in range(1,V+1) :
        if visited[j] == 0:
            visited[j] = 1 # 시작 색 지정
            dfs(j)

    print(ans)
    