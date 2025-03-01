from collections import deque
def bfs(weight) : # 현재 최대 중량
  q = deque()
  q.append(s)
  v = [0]*(N+1)
  v[s] = 1

  while q : # 방문할 수 있을 때까지 인접한 노드 방문
    c = q.popleft()
    for i,w in bridge[c] : # i는 연결된 섬 번호, w는 중량
      if not v[i] and w >= weight : # 방문 안했고 최대 중량보다 더 크면,
        v[i] = 1
        q.append(i)

  if v[e] : return 1    # 방문 가능하면 1 출력
  else : return 0

N,M = map(int,input().split())
bridge = [[] for _ in range(N+1)]
for i in range(M) :
  a,b,c = map(int,input().split())
  bridge[a].append([b,c])
  bridge[b].append([a,c])

s,e = map(int,input().split())

result = 0
low = 0                 # 현재 가능한 최소 중량 제한
high = 1000000000    # 현재 가능한 최대 중량 제한
while low <= high:
  mid = (low+high)//2   # 현재 검사할 중량 제한
  if bfs(mid) :         # mid로 중량 제한했을 때, 지나갈 수 있는 다리가 있는지?
    result = mid
    low = mid+1       # 더 무거운 무게도 가능한지 시도
  else : 
    high = mid - 1       # 너무 무거우니까 무게 줄이기

print(result)