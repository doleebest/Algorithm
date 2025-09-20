N,M = map(int, input().split())
si,sj,dr = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# dr : 북  동  남   서
di = [-1, 0 , 1, 0]
dj = [0,  1, 0, -1]

def solve(ci,cj,dr) :
    cnt = 0     # 청소한 공간 수
    while 1 :   # 청소기가 더이상 움직이지 못할 때 종료
        # 1. 현재 위치 청소
        arr[ci][cj] = 2
        cnt+=1
        
        # 2. 왼쪽 방향으로 순서대로 탐색해서 미청소 영역이 있는 경우 이동/방향설정, 없으면 후진
        flag = 1
        while flag ==1 :
            # 왼쪽부터 네 방향 중 빈칸 미청소 영역 있는 경우
            for nd in ((dr+3)%4, (dr+2)%4, (dr+1)%4, dr) :
                ni,nj = ci+di[nd], cj+dj[nd]
                if arr[ni][nj] == 0 :   # 미청소 영역
                    ci, cj, dr = ni, nj, nd # 갱신
                    flag = 0
                    break # for 문, 가까운 while문 탈출 -> 맨 위 while문으로! 그리고 1. 현재위치 청소
            else :      # 4 방향 모두 미청소 영역 없으면
                bi, bj = ci-di[dr], cj-dj[dr]   # 후진할 위치 계산
                if arr[bi][bj] == 1 :           # 벽이면 종료
                    return cnt
                else : 
                    ci,cj = bi,bj   # 후진
    
    # 이곳에 도달할 리는 없겠지만..
    return -1

ans = solve(si,sj,dr)
print(ans)