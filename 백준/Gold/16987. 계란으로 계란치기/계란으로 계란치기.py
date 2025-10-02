def dfs(n,cnt) :
    global ans
    if n==N :               # 종료조건 : 모든 계란을 손에 들고 부딪히기 완료
        ans = max(ans, cnt)
        return

    if arr[n][0]<=0 :       # 현재 계란이 깨진 경우 -> 다음 계란으로
        dfs(n+1, cnt)
    else :
        flag = False        # 한번도 안 부딪힌 경우 -> 그래도 다음 계란으로 가야함
        for j in range(N) : # 현재 계란이 안깨진 상태 -> 하나씩 부딪혀보기
            if n==j or arr[j][0]<=0 :
                continue
            flag = True
            arr[n][0] -= arr[j][1]
            arr[j][0] -= arr[n][1]
            dfs(n+1, cnt+int(arr[n][0]<=0)+int(arr[j][0]<=0))
            arr[n][0] += arr[j][1]  # 원상 복구
            arr[j][0] += arr[n][1]

        if flag == False :
            dfs(n+1, cnt)

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = 0

# 계란 index, 깨진 계란 개수
dfs(0,0)
print(ans)