from collections import deque

def bfs() :
  # q생성, v 생성
  q = deque()
  v = [[0]*M for _ in range(N)]

  cnt = 0
  for i in range(N) :
    for j in range(M) :
      if tomato[i][j] == 0 :
        cnt+=1
      elif tomato[i][j] == 1 :
        q.append((i,j))
        v[i][j] = 1 # 순회의 시작점이 될 부분. 안 익은 토마토는 곧 방문할 곳임.
  
  while q :
    ci,cj = q.popleft()
    
    for di,dj in ((-1,0), (1,0), (0,1), (0,-1)) :
      ni,nj = ci+di, cj+dj
      if 0<=ni<N and 0<=nj<M and v[ni][nj] == 0 and tomato[ni][nj]==0:
        v[ni][nj] = v[ci][cj]+1
        q.append((ni,nj))
        cnt-=1
    
  if cnt == 0:
    return v[ci][cj] -1
  else :
    return -1

M,N = map(int, input().split())
tomato = [list(map(int,input().split())) for _ in range(N)]
ans = bfs()
print(ans)
