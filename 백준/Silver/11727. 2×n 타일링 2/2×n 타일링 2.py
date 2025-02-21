n = int(input())

# [1] dp[] table정의
# [2] dp[i]: 2*i 길이의 직사각형을 만드는 방법의 수
dp= [0] * (n+1)

# [3] dp[]의 초기값 설정
# n==1인 경우 dp[2]를 설정하면 dp[2]가 존재하지 않아 index오류가 발생
# dp[1], dp[2] = 1, 3 (x)
dp[0], dp[1] = 1, 1

for i in range(2,n+1) :
  dp[i] = dp[i-2]*2 + dp[i-1]

ans = dp[n] % 10007
print(ans)