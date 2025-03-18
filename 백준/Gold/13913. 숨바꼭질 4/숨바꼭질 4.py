def bfs(n, lst) :
  global cnt
  q.append(n)
  v[n]=1
  parent[n] = -1  # 시작 위치의 부모 없음

  while q :
    c = q.pop(0)
    
    if c == K : # 종료 조건
      return v[K]-1

    for n in (c-1,c+1, c*2):
      if 0<=n<100001 and v[n] == 0 :
        q.append(n)
        v[n] = v[c]+1 # 현재 위치까지 걸린 시간 저장
        parent[n] = c  # 부모 정보 저장

  return -1  # 도달 불가능한 경우

def backtrack(n):  # 부모 배열을 이용한 역추적
    path = []
    while n != -1:
        path.append(n)
        n = parent[n]  # 부모 노드 따라가기
    return path[::-1]  # 정방향으로 뒤집기

N,K = map(int, input().split())
v = [0]*100001
q=[]
parent = [-1] * 100001  # 부모 정보 저장

print(bfs(N,[])) # 시간 출력
print(*backtrack(K))