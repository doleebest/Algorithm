N = int(input())
area = [list(map(int,input().split())) for _ in range(N)]
cnt = [0]*101

def bfs(si,sj) :
    global island_cnt
    q = []
    q.append((si,sj))
    visited[si][sj] = 1
    
    while q :
        ci,cj = q.pop()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)) :
            ni = ci+di
            nj = cj+dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0 :
                visited[ni][nj] = 1
                q.append((ni,nj))
    
    island_cnt += 1

# 높이에 따라 달라진다.
for height in range(0,101) :
    island_cnt = 0
    visited = [[0]*N for _ in range(N)]
    # 배열을 돌면서 잠기는 곳을 모두 방문 표시
    for i in range(N) :
        for j in range(N) :
            if area[i][j] <= height :
                visited[i][j] = 1
    
    for k in range(N) :
        for l in range(N) :
            if visited[k][l] == 0:
                bfs(k,l)
    cnt[height] = island_cnt

ans =  max(cnt)
print(ans)