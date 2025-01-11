def dfs(n,sm) : 
    global ans
    # 종료조건 : 가능한 n을 종료에 관련된 것으로 정의
    if n >= N : 
        ans = max(ans, sm)
        return 
    
    # 하부 호출 : 화살표 개수만큼 호출
    if n+T[n] <= N : # 상담하는 경우 (퇴사일 전 상담이 완료 가능)
        dfs(n+T[n], sm + P[n])
    dfs(n+1, sm) # 상담하지 않는 경우 (항상 가능)

N = int(input())
T = [0]*N
P = [0]*N
for i in range(N) : 
    T[i], P[i] = map(int, input().split())
    
ans = 0
dfs(0,0)
print(ans)