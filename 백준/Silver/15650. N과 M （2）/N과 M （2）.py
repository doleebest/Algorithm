def dfs(n,s,lst) :
  if n==M:      # M개 선택 완료
    ans.append(lst)
    return
  
  for j in range(s, N+1) :
    dfs(n+1, j+1, lst+[j])

N,M = map(int, input().split())
ans = []
# dfs(1,[])     # 이진트리
dfs(0,1,[])   # 멀티트리
for lst in ans :
  print(*lst) 