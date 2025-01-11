N = int(input())
T = [0] * N
P = [0] * N

for i in range(N): 
    T[i], P[i] = map(int, input().split())
    
dp = [0] * (N + 1)  # dp 배열 초기화

for n in range(N - 1, -1, -1):  # 뒤에서 앞으로 계산
    if n + T[n] <= N: 
        dp[n] = max(dp[n + 1], dp[n + T[n]] + P[n])  # 상담 가능
    else: 
        dp[n] = dp[n + 1]  # 상담 불가능

print(dp[0])  # 최대 수익 출력
