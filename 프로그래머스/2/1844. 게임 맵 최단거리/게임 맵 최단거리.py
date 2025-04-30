def solution(maps):
    m = len(maps[0])
    n = len(maps)
    visited = [[0]*m for _ in range(n)]
    q = []
    visited[0][0] = 1
    q.append((0,0)) # 출발
    
    while q :
        ci,cj = q.pop(0)
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)) :
            ni, nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<m and maps[ni][nj]==1 :
                if visited[ni][nj]==0 : # 범위내, 벽이 아니고, 미방문
                    q.append((ni,nj))
                    visited[ni][nj] = 1
                    maps[ni][nj] = maps[ci][cj] + 1
    if maps[n-1][m-1] == 1: return -1
    else : return maps[n-1][m-1] 