from collections import deque

# bfs
def bfs(si,sj) :
  q.append((si,sj))
  visited[si][sj] = 1
  while q :
    ci,cj = q.popleft()
    for di,dj in ((-1,0), (1,0), (0,-1), (0,1)) :
      ni,nj = ci+di, cj+dj
      if 0<=ni<N and 0<=nj<N and arr[ci][cj] == arr[ni][nj] and not visited[ni][nj] :
        visited[ni][nj] = 1
        q.append((ni,nj))

N= int(input())
arr = [list(input()) for _ in range(N)]
q = deque()

# 적록 색약이 아닌 경우
visited = [[0] * N for _ in range(N)]
cnt1 = 0
for i in range(N) :
  for j in range(N) :
    if not visited[i][j] :
      bfs(i,j)
      cnt1+=1

# 적록 색약인 경우
for i in range(N) :
  for j in range(N) :
    if arr[i][j] == 'G' :
      arr[i][j] = 'R'

visited = [[0] * N for _ in range(N)]
cnt2 = 0
for i in range(N) :
  for j in range(N) :
    if not visited[i][j] :
      bfs(i,j)
      cnt2+=1

print(cnt1,cnt2)