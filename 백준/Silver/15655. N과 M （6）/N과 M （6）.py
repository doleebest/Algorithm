def dfs(cnt, s, lst) :
  if cnt == M :
    ans.append(lst)
    return  # 종료
  
  for j in range(s, N) :  # 오름차순 수열을 위해서 선택한 숫자 이후 값부터 선택
    if v[j] == 0 :
      v[j] = 1
      dfs(cnt+1, j+1, lst+[arr[j]])
      v[j] = 0

N,M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []
v = [0]*N

# 선택한 개수, 시작 위치, lst
dfs(0,0,[])

for lst in ans :
  print(*lst)