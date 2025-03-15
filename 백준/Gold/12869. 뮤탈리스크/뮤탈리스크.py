n = int(input())
scv = list(map(int,input().split()))
scv.extend([0,0])

dp = [[[0]*61 for _ in range(61)] for _ in range(61)] #각 위치에 도달하는 횟수 저장
dp[scv[0]][scv[1]][scv[2]] = 1     # 일단 방문표시하고 나중에 -1. 방문표시를 해야 if문을 통과해서 attack 시작이 가능

attack = [(9,3,1), (9,1,3), (1,9,3), (1,3,9), (3,1,9), (3,9,1)]
for i in range(60,-1,-1) :
  for j in range(60,-1,-1) :
    for k in range(60,-1,-1) :
      if dp[i][j][k] > 0 :
        for a in attack :
          ni = i-a[0] if i-a[0]>=0 else 0
          nj = j-a[1] if j-a[1]>=0 else 0
          nk = k-a[2] if k-a[2]>=0 else 0
          # 처음 도착한 경우 or 더 적은 횟수로 도착하는 경우에만 업데이트
          if dp[ni][nj][nk] == 0 or dp[ni][nj][nk] > dp[i][j][k]+1:
            dp[ni][nj][nk] = dp[i][j][k]+1
print(dp[0][0][0]-1)