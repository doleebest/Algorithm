N, M, K = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
q = []
ans = -1e10

def dfs(x, y, d, s): 
    global ans
    if d == K:
        ans = max(ans, s) # 현재까지의 최대값 갱신
        return
    else:
        for i in range(x, N):
            for j in range(y if i == x else 0, M):
                if [i, j] not in q:
                    if ([i + 1, j] not in q) and ([i - 1, j] not in q) and ([i, j + 1] not in q) and ([i, j - 1] not in q):
                        q.append([i, j]) # 방문하면 q에 넣는다.
                        dfs(i, j, d + 1, s + a[i][j])
                        q.pop()


dfs(0, 0, 0, 0)
print(ans)