n = int(input())

# dp 2차원으로 설계/반복처리
dp = [[0]*10 for _ in range(n+1)]

for i in range(0,10) :
  dp[1][i] = 1

for i in range(2,n+1) :
  for j in range(0,10) :
    dp[i][j] = sum(dp[i-1][j:])

ans = 0
for i in range(10) :
  ans += dp[n][i]
print(ans%10007)
