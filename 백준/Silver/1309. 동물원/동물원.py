N =  int(input())

# [1] 메모리 사용량이 많음
# dp = [[0]*3 for _ in range(N)]
# dp[0] = [1]*3
#
# for i in range(1, N):
#     dp[i][0] = sum(dp[i-1])%9901
#     dp[i][1] = (dp[i-1][0]+dp[i-1][2])%9901
#     dp[i][2] = (dp[i-1][0]+dp[i-1][1])%9901
# ans = sum(dp[N-1])

# [2] 변수를 사용해서, 우변에서 한 번에 연산후 튜플로 좌변 대입(메모리적게 소모, 속도빠름)
n0 = n1 = n2 = 1
for i in range(1, N):
    n0, n1, n2 = (n0+n1+n2)%9901, (n0+n2)%9901, (n0+n1)%9901
ans = n0+n1+n2
print(ans%9901)