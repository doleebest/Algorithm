import sys
import heapq
input = sys.stdin.readline

# 입출력
N, E = map(int, input().split())
edges = [[] for i in range(N+1)]

# 무방향 그래프 : 하나의 간선에 대해 양쪽 노드 둘 다 정보 저장
for i in range(E):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))
    edges[b].append((a, c))
    
v1, v2 = map(int, input().split())

# 다익스트라 알고리즘
# 하나의 출발 노드로부터 모든 노드로의 최단 거리를 구하고, 그 중에서 목표 노드로의 최단 거리만 리턴)
def dijkstra(start, end):
    route = [sys.maxsize]*(N+1)
    route[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        cnt_w, cnt_node = heapq.heappop(q) # 가장 거리가 짧은 노드를 꺼낸다.
        
        if route[cnt_node] < cnt_w: # cnt_node로 가는 더 짧은 경로가 이전에 처리된 경우
            continue # 무시하고 건너뜀 -> while
        
        for adjacency_node, adjacency_w in edges[cnt_node]: # cnt_node와 연결된 모든 이웃 노드(adjacency_node)를 검사
            cal_w = route[cnt_node] + adjacency_w # 현재노드까지 온 거리 + 이웃노드로 가는 거리
            
            if cal_w < route[adjacency_node]: # 만약 새로운 거리가 이전에 저장된 adjacency_node까지의 거리보다 짧으면
                route[adjacency_node] = cal_w # 갱신해주기
                heapq.heappush(q, (cal_w, adjacency_node))
    
    return route[end]

# 최단 경로는 두 가지 가능한 경우의 수 : (1 > v1 > v2 > N or 2 > v2 > v1 > N)
route1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
route2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

# 만약 위 식에서 하나의 최단 거리라도 존재하지 않으면 그 경로의 값은 sys.maxsize가 된다.
# 이 경우를 조건문으로 걸러주어 상황에 맞는 올바른 답을 출력해준다.
if route1 >= sys.maxsize and route2 >= sys.maxsize:
    print(-1)
else:
    print(min(route1, route2))