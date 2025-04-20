N,D = map(int, input().split())
shortcuts = []

# 지름길 입력
for _ in range(N) :
  start, end, cost = map(int,input().split())
  if end <= D : shortcuts.append((start, end, cost))

# 거리 배열
dist = [i for i in range(D+1)]  # dist[i] = 0부터 i까지의 최소 거리

# 0부터 D까지 순차적으로 확인
for i in range(D+1) :
  if i+1 <= D :
    dist[i+1]  = min(dist[i+1],dist[i] + 1)

  # 지름길 사용가능한지 확인
  for start, end, cost in shortcuts :
    if start == i and dist[end] > dist[i]+cost : # 지금 i 위치에서 출발하는 지름길이 있는 경우
      dist[end] = dist[i] + cost

print(dist[D])

