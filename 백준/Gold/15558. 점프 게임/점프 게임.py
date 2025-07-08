from collections import deque

n, k = map(int, input().split())
left  = list(map(int, input().strip()))   # 공백 없이 0/1 나열
right = list(map(int, input().strip()))
board = [left, right]                     # board[줄][칸]

def bfs():
    visited = [[False]*n for _ in range(2)]
    visited[0][0] = True
    q = deque([(0, 0, 0)])                # (칸, 줄, 시간)

    while q:
        ci, cj, ck = q.popleft()
        for di, swap in [(+1, 0), (-1, 0), (k, 1)]:
            ni = ci + di
            nj = cj ^ swap
            nk = ck + 1

            # 1) 범위 넘으면 클리어
            if ni >= n:
                return 1

            # 2) 유효 범위 && 아직 안 사라짐 && 안전칸 && 미방문
            if 0 <= ni < n and ni >= nk and board[nj][ni] == 1 and not visited[nj][ni]:
                visited[nj][ni] = True
                q.append((ni, nj, nk))

    return 0

print(bfs())
