import sys
INF = 1000*1000+1
R, G, B = 0, 1, 2

N = int(sys.stdin.readline().rstrip())
cost = [[-1, -1, -1]] # 인덱스 0번 집은 사용 안 함. 이후 인덱스 1부터 집을 세려고

# 각 집을 빨강, 초록, 파랑으로 칠하는 비용
for _ in range(N):
    cost.append(list(map(int, sys.stdin.readline().rstrip().split())))

answer = INF
for color in [R,G,B]: # 이제 집을 칠할 것!
    dp = [[-1]*3 for _ in range(N+1)] # 어떤 색으로 칠할 지 초기화

    dp[1] = [INF, INF, INF] # 1번집 칠하고
    dp[1][color] = cost[1][color]
    
    '''
    집 i번을 빨강으로 칠하려면, i-1번 집은 초록이나 파랑. (옆집은 다른 색이어야 하므로)
	그래서 dp[i][R]은 i-1번 집을 초록이나 파랑으로 칠한 최소비용 + i번 집 빨강비용
	'''

    for i in range(2, N+1):
        dp[i][R] = min(dp[i-1][G], dp[i-1][B]) + cost[i][R]
        dp[i][G] = min(dp[i-1][R], dp[i-1][B]) + cost[i][G]
        dp[i][B] = min(dp[i-1][R], dp[i-1][G]) + cost[i][B]
    dp[N][color] = INF # 1번 집과 N번 집은 서로 다른 색이어야 함. 만약 1번 집을 빨강(R)으로 칠했으면, N번 집이 빨강(R)으로 끝나는 경우는 무조건 버려지도록 값을 매우 크게
    answer = min(answer, min(dp[N]))
print(answer)