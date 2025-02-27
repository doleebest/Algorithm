def dfs(n,lst) :
  if n==M :
    ans.append(lst)
    return

  for j in range(0,N) :
    if v[j] == 0:
      v[j] = 1
      dfs(n+1, lst+[arr[j]])
      v[j] = 0

N,M = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort()
v = [0]*(N)
ans = []
dfs(0,[])
for lst in ans :
  print(*lst)