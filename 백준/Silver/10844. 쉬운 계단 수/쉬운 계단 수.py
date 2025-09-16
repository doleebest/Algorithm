dp = [[-1]*10 for _ in range(101)]
def solve(n,i):
    if n==1 :
        if i==0 : 
            return 0
        return 1
    
    if dp[n][i] != -1 :
        return dp[n][i] % 1000000000 # 실수 방지
    
    if i>=1 and i<=8 :
        dp[n][i] = solve(n-1, i-1) + solve(n-1,i+1)
    if i==0 :
        dp[n][i] = solve(n-1,1)
    if i==9 :
        dp[n][i] = solve(n-1,8)
    
    return dp[n][i] % 1000000000

n = int(input())
ans=0
for i in range(0,10) :
    ans+=solve(n,i)
print(ans% 1000000000)