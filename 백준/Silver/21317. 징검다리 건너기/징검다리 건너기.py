def solve(i, is_jump) :
    if i == N :
        return 0

    if dp[i][is_jump] != -1:
        return dp[i][is_jump]

    res = float('inf')

    if i + 1 <= N:
        res = min(res,small[i] + solve(i + 1, is_jump))
    if i + 2 <= N:
        res = min(res, big[i] + solve(i + 2, is_jump))

    if not is_jump and i+3 <=N:
        res = min(res, jump + solve(i+3,True))

    dp[i][is_jump] = res
    return res # current 돌에서 마지막 돌까지 가는데 필요한 최소 에너지

N = int(input())
small = [0]*(N+1)
big = [0]*(N+1)
for i in range(1,N) :
    a,b = map(int,input().split())
    small[i] = a
    big[i] = b
jump = int(input())
dp = [[-1]*2 for _ in range(N+1)] # 0~N
print(solve(1,False))