import sys
sys.setrecursionlimit(10**6)

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
color = [0,1,2] # r,g,b
tmp = []
INF = int(1e9)

# dp[a][b] = solve(a,b)
dp = [[-1]*3 for _ in range(n)] # 한번 구한 (a,b) 결과를 저장해두기 (메모이제이션)

def solve(a,b) : # a번째에서 b의 컬러를 칠했을 때 생기는 a번째 까지의 최적해    
    if dp[a][b] != -1 : # 이미 계산된 적이 있음
        return dp[a][b]
    
    if a ==0 : # a가 0이면 그냥 a번째 집을 b색으로 칠했을 때 최소비용
        dp[0][b] = arr[0][b]
        return arr[0][b]

    min_val = INF
    for i in color :
        if b != i : # 색깔이 같으면 패스하고
            # 색깔이 다르면 그 비용을 고려해보기 위해서 tmp에 추가해놓음
            min_val = min(min_val,solve(a-1,i))
    dp[a][b] = arr[a][b]+min_val
    
    return dp[a][b] # 그러고 tmp 중에 작은거 골라서 더해주기

answer = min(solve(n-1,0),solve(n-1,1),solve(n-1,2))
print(answer)
