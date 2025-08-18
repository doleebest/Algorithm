t = int(input())
nums = [int(input()) for _ in range(t)]
dp = [[0]*4 for _ in range(10001)]

for k in range(1,4) : 
    dp[0][k] = 1 # n = 0인 경우(아무것도 안쓰는 경우) 1가지

for n in range(1,10001) :
    for k in range(1,4) :
            dp[n][k] = dp[n][k-1] 
            if n-k >= 0 : # 이런 경우에만
                dp[n][k] += dp[n-k][k] # 더해준다.

for n in nums :
    print(dp[n][3])