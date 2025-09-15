n = int(input())
p = list(map(int,input().split()))

# 함수가 뭘 리턴해야하는지 생각해보자.
# k장을 만들 때 드는 최소비용을 메모이제이션으로 저장해두기
INF = 10**9
dp = [INF]*(n+1)
dp[0] = 0

def solve(k) :
    if k == 0 :
        return 0
    
    if dp[k] != INF :
        return dp[k]
    for i in range(0,n) :
        if k-(i+1) >=0 :
            dp[k] = min(p[i]+solve(k-(i+1)),dp[k])
    return dp[k]

print(solve(n))