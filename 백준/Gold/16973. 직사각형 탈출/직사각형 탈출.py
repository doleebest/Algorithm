from collections import deque
import sys


input = sys.stdin.readline

N, M = map(int, input().split())							# 격자판의 크기 (행, 열)
maps = [list(map(int, input().split())) for _ in range(N)]	# 격자판의 각 칸의 정보 - 0은 빈칸, 1은 벽
H, W, Sr, Sc, Fr, Fc = map(int, input().split())			# 직사각형의 크기 H, W, 시작 좌표 Sr, Sc, 도착 좌표 Fr, Fc

# 4방
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

# 벽 위치 저장
walls = []

for i in range(N):
    for j in range(M):
        if maps[i][j] == 1:
            walls.append((i, j))


def move(r, c):

    queue = deque()

    queue.append((r, c))
    maps[Sr][Sc] = 2

    while queue:

        nowr, nowc = queue.popleft()

        if nowr == Fr and nowc == Fc:
            return maps[Fr][Fc] - 2

        for d in range(4):

            nr = nowr + dr[d]
            nc = nowc + dc[d]

            # 직사각형은 격자판 안에 있어야 함 / 직사각형이 놓여 있는 칸에는 벽이 없음
            if nr < 0 or nc < 0 or nr > (N - H) or nc > (M - W) or maps[nr][nc] or not check(nr, nc):
                continue

            queue.append((nr, nc))
            maps[nr][nc] = maps[nowr][nowc] + 1

    return -1


def check(startr, startc):
    minr, maxr = startr, startr + H
    minc, maxc = startc, startc + W

    for (r, c) in walls:
        if minr <= r < maxr and minc <= c < maxc:
            return False
        
    return True


Sr, Sc, Fr, Fc = Sr-1, Sc-1, Fr-1, Fc-1

print(move(Sr, Sc))