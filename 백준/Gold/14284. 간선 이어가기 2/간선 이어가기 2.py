import heapq
import sys
INF = sys.maxsize

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if distance[now] < d:
            continue
        for v, w in graph[now]:
            cost = d + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
s, t = map(int, input().split())
dijkstra(s)
print(distance[t])