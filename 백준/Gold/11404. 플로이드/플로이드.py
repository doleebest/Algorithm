import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한대 값 설정

n = int(input())  # 도시 수
m = int(input())  # 버스 수

# 거리 배열 초기화
dist = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신 -> 자기 자신 비용은 0
for i in range(1, n + 1):
    dist[i][i] = 0

# 버스 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # 같은 노선이 여러 번 나올 수 있으므로 최소 비용만 저장
    dist[a][b] = min(dist[a][b], c)

# 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):       # 경유지
    for i in range(1, n + 1):   # 출발지
        for j in range(1, n + 1):  # 도착지
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# 결과 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 갈 수 없는 경우 0 출력
        if dist[i][j] == INF:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()
