s1 = input()
s2 = input()

N, M = len(s1), len(s2)
s1 = " " + s1
s2 = " " + s2

# 초기값 
dp = [[0] * (M + 1) for _ in range(N + 1)]

# DP Table 갱신하기
for n in range(1, N + 1):
    for m in range(1, M + 1): # dp[n][m]
        if s1[n] == s2[m]:
            dp[n][m] = dp[n - 1][m - 1] + 1
        else: 
            dp[n][m] = max(dp[n - 1][m], dp[n][m - 1])

print(dp[N][M])