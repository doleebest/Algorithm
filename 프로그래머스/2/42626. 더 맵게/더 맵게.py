# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
import heapq
def solution(scoville, K):
    heapq.heapify(scoville) # heap 초기화
    cnt=0
    while len(scoville) > 1:
        a = heapq.heappop(scoville) # 가장 안 매운 element
        if a < K :
            cnt += 1
            b = heapq.heappop(scoville)
            heapq.heappush(scoville, a+b*2)
    if scoville[0] >= K : return cnt
    else : return -1