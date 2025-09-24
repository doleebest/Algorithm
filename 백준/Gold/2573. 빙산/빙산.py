from collections import deque
N,M = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
island = 0
year = 0
ice = 0

# 시간 초과 해결 : 빙산이 있는 부분의 좌표만 저장
icebergs = [(i,j) for i in range(N) for j in range(M) if arr[i][j]>0]

# 덩어리 개수를 세기 위한 bfs
def bfs(si,sj) :
    q = deque()
    q.append((si,sj))
    visited[si][sj] = 1
    while q :
        ci,cj = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)) :
            ni = ci+di
            nj = cj+dj
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0 and arr[ni][nj]!=0 :
                q.append((ni,nj))
                visited[ni][nj] = 1
                
while True : # 섬이 두개가 되기 전까지 반복'
    melt = [[0]*M for _ in range(N)]
    # 빙산 높이 줄어들게 하기
    for i,j in icebergs :
        if arr[i][j] !=0 :
            ice=0
            for di, dj in ((-1,0),(1,0),(0,-1),(0,1)) :
                ni = i+di
                nj = j+dj
                if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0:
                    ice+=1
            melt[i][j] = ice
               
    # 놓쳤던 포인트! 한번에 뺴줘야함. 안 그러면 주변의 값이 바뀌어버림. 
    # 시간 초과 해결 : iceberg 안에 있는 값들만 바꿔주기
    new_icebergs = []
    for p,q in icebergs :
        arr[p][q] = max(arr[p][q]-melt[p][q],0)
        if arr[p][q] > 0 :
            new_icebergs.append((p,q))
    icebergs = new_icebergs
    
    island = 0
    visited = [[0]*M for _ in range(N)]
    # 빙산 덩어리 개수 세기
    for k,l in icebergs :
        if arr[k][l] != 0 and visited[k][l] == 0:
            bfs(k,l)
            island+=1
    
    year+=1
    
    if island == 0 :
        print(0)
        break
    elif island >= 2 : 
        print(year)
        break