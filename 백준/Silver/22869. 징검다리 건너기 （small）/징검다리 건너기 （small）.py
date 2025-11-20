from sys import setrecursionlimit
setrecursionlimit(10**6)
def solve(i) :
    if dp[i] != -1 :
        return dp[i]

    if i==N-1 :
        dp[i] = True
        return True

    dp[i] = False

    for j in range(i+1, N) :
        jump_cost = (j - i) * (1 + abs(A[i] - A[j]))
        if jump_cost <= K :
            if solve(j) == True :
                dp[i] = True
                break
    return dp[i]

INF = 999999999
N,K = map(int,input().split())
A = list(map(int,input().split()))
dp = [-1]*N
print("YES" if solve(0) else "NO")
