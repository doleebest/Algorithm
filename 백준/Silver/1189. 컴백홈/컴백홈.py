R,C,K = map(int,input().split())
road = [list(input().strip()) for _ in range(R)]

ans=0
visited = [[0]*C for _ in range(R)]
def dfs(si,sj,cnt,goal,visited) :
    global ans
    if cnt == goal and (si,sj) == (0,C-1) :
        ans+=1
        return

    visited[si][sj] = 1
    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)) :
        ni = si+di
        nj = sj+dj
        if 0<=ni<R and 0<=nj<C and visited[ni][nj] ==0 and road[ni][nj] == '.' :
            dfs(ni,nj,cnt+1,goal,visited)
    
    visited[si][sj] = 0 # 백트래킹!

dfs(R-1,0,1,K,visited)
print(ans)