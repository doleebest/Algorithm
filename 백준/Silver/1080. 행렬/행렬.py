# 알고리즘? 그리디
# 왜냐하면 당시에 최선의 선택을 해야하고
# 그 선택이 이후에도 영향을 미침 (반대로 dp는 각 단위가 독립적임)
# bfs는 visited 경우의 수가 너무 많음. 안됨

N,M = map(int,input().split())
A = [str(input()) for _ in range(N)]
for i in range(N) :
    A[i] = [int(item) for item in A[i]]

B = [str(input()) for _ in range(N)]
for i in range(N) :
    B[i] = [int(item) for item in B[i]]

# 토글을 여러번 하기
# 만약에 같지 않다면 돌려놔야하나...? 백트래킹?
# -> 아닌가 최소 횟수니까 그냥 계속 누적?
# 어디부터 토글? 중간에 토글을 건너뛸 수 있게 해야하나?
# 순서 ?바꿔야하는 애인가 아닌가
cnt = 0
for k in range(N) :
    for l in range(M) :
        if A[k][l]!=B[k][l] :
            if k+2 < N and l+2 <M :
                for i in range(k, k + 3):
                    for j in range(l, l + 3):
                        A[i][j] ^= 1
                cnt+=1
if A==B :
    print(cnt)
else :
    print(-1)