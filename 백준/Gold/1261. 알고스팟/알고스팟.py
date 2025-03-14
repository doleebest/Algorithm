from collections import deque

M,N = map(int, input().split())   # 가로, 세로
arr = [list(map(int, input().strip())) for _ in range(N)]

dist = [[-1]*M for _ in range(N)]   # 각 위치까지의 최소 벽 파괴 횟수를 저장할 배열 (초기값: -1)

q=deque()       # 0-1 bfs를 위한 deque
q.append((0,0))
dist[0][0] = 0  # 시작점은 벽을 부순 횟수가 0

while q :
  ci,cj = q.popleft()
  for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
      ni, nj = ci + di, cj + dj
      if 0 <= ni < N and 0 <= nj < M and dist[ni][nj] == -1 :
        if arr[ni][nj] == 0:
          # 빈칸(0)일 때 우선 탐색 -> 앞에 추가
          dist[ni][nj] = dist[ci][cj]
          q.appendleft((ni, nj))
        else :
          # 빈칸(1)일 때 나중 탐색 -> 뒤에 추가
          dist[ni][nj] = dist[ci][cj] + 1
          q.append((ni, nj))

# 도착지점(N-1, M-1)까지의 최소 벽 파괴 횟수 출력
print(dist[N-1][M-1])