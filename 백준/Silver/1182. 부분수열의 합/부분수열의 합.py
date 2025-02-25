def dfs(n, sm, cnt) :
  global ans
  # 종료조건 (n에 관련) + 정답 관련 처리
  if n==N : # 끝까지 다 탐색하고
    if sm==S and cnt>0 : # 합이 s이면
      ans+=1 # 경우의 수 하나 증가!
    return

  # 하부 함수 호출
  dfs(n+1, sm+lst[n], cnt+1) # 이 원소를 포함할 수도 있고
  dfs(n+1, sm, cnt) # 안할 수도 있고

N,S = map(int,input().split())  # N개의 정수로 이루어진 수열, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S
lst = list(map(int,input().split()))
ans = 0  # 경우의 수  
dfs(0,0,0)
print(ans)