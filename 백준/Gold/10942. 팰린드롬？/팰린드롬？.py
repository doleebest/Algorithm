import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))  # 인덱스를 1부터 시작하기 위해 앞에 0 추가

m = int(input())
queries = [tuple(map(int, input().split())) for _ in range(m)]

# dp[i][j] = arr[i..j]가 팰린드롬인지 여부
dp = [[False] * (n+1) for _ in range(n+1)]

# 길이 1
for i in range(1, n+1):
    dp[i][i] = True

# 길이 2
for i in range(1, n):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = True

# 길이 3 이상
for length in range(3, n+1):       # 부분 수열의 길이
    for i in range(1, n-length+2):
        j = i + length - 1
        if arr[i] == arr[j] and dp[i+1][j-1]:
            dp[i][j] = True

# 쿼리 답변
for s, e in queries:
    print(1 if dp[s][e] else 0)
