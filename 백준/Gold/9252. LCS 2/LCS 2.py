# dp 테이블 : a의 처음 i개와 b의 처음 j개를 비교했을 때의 lcs 길이
arr_a = input()
arr_b = input()

n = len(arr_a)
m = len(arr_b)

dp = [[0]*(m+1) for _ in range(n+1)]

# 0번째 행/열은 당연히 0이므로 0으로 설정함
for i in range(n+1) :
    for j in range(m+1) :
        if i >=1 and j >=1 : 
            if arr_a[i-1] == arr_b[j-1] : 
                dp[i][j] = dp[i-1][j-1]+1
            elif arr_a[i-1] != arr_b[j-1] : 
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# dp table을 역추적 해야함.
i,j = n,m
string = ""
while i>0 and j>0 :
    if arr_a[i-1] == arr_b[j-1] :
        # 같으면 lcs에 포함됨. 그 문자는 LCS의 일부 
        # 따라서 문자열에 추가
        string+=arr_a[i-1]
        i-=1
        j-=1
    else :
        # 다르면 dp[i-1][j], dp[i][j-1] 중 하나를 버리고 더 긴 쪽으로 따라가야함.
        if dp[i-1][j]>=dp[i][j-1] :
            i-=1
        else: 
            j-=1

print(dp[n][m])
print(''.join(string[::-1]))