import sys

n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]  # sys.stdin.readline() 사용
visited = [0] * n
ans = float('inf')  # 최소값을 구하기 위해 초기값을 무한대 설정

def cal():
    global ans
    star, link = 0, 0
    for i in range(n):
        for j in range(n):
            if visited[i] and visited[j]:
                star += arr[i][j]
            elif not visited[i] and not visited[j]:
                link += arr[i][j]
    ans = min(ans, abs(star - link))  # 최소 차이 갱신

def solve(iter):
    global ans
    if iter == n:
        # 한 팀이 비어있는 경우는 제외
        if 0 < sum(visited) < n:
            cal()
        return

    visited[iter] = 1
    solve(iter + 1)
    visited[iter] = 0
    solve(iter + 1)

solve(0)
print(ans)
