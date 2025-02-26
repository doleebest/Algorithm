def dfs(n, lst) :
  if n>N :             # 종료 조건
    if len(lst) == M : # M개짜리 수열 => 정답처리
      ans.append(lst)
    return

  dfs(n+1, lst+[n])  # 선택하는 경우
  dfs(n+1, lst)     # 선택하지 않는 경우

N,M = map(int, input().split())
ans = []
dfs(1,[])
for lst in ans:
  print(*lst)
