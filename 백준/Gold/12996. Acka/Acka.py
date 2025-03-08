MOD = 1000000007

def count_album_ways(S, d, k, h):
    # DP 테이블 초기화
    DP = [[[[0] * (S+1) for _ in range(S+1)] for _ in range(S+1)] for _ in range(S+1)]
    
    # 초기 상태
    DP[0][0][0][0] = 1
    
    # DP 채우기
    for s in range(1, S+1):
        for i in range(S+1):
            for j in range(S+1):
                for l in range(S+1):
                    DP[s][i][j][l] = 0
                    if i > 0: DP[s][i][j][l] = (DP[s][i][j][l] + DP[s-1][i-1][j][l]) % MOD
                    if j > 0: DP[s][i][j][l] = (DP[s][i][j][l] + DP[s-1][i][j-1][l]) % MOD
                    if l > 0: DP[s][i][j][l] = (DP[s][i][j][l] + DP[s-1][i][j][l-1]) % MOD
                    if i > 0 and j > 0: DP[s][i][j][l] = (DP[s][i][j][l] + DP[s-1][i-1][j-1][l]) % MOD
                    if i > 0 and l > 0: DP[s][i][j][l] = (DP[s][i][j][l] + DP[s-1][i-1][j][l-1]) % MOD
                    if j > 0 and l > 0: DP[s][i][j][l] = (DP[s][i][j][l] + DP[s-1][i][j-1][l-1]) % MOD
                    if i > 0 and j > 0 and l > 0: DP[s][i][j][l] = (DP[s][i][j][l] + DP[s-1][i-1][j-1][l-1]) % MOD
    
    return DP[S][d][k][h]

# 입력 받기
S, d, k, h = map(int, input().split())
print(count_album_ways(S, d, k, h))
