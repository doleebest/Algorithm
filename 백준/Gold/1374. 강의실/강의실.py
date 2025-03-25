import heapq

def classroom(n, lectures) :
  # 시작 시간을 기준으로 정렬
  lec.sort(key = lambda x : x[1])

  # 우선순위 큐(최소 힙) 선언
  min_heap = []

  # 첫 강의의 종료 시간을 힙에 삽입. 어차피 우리가 고려하는 것은 종료시간! 종료 시간만 삽입하면 됨.
  heapq.heappush(min_heap,lec[0][2])

  for i in range(1,n) :
    start, end = lec[i][1], lec[i][2]

    if min_heap[0] <= start :   # 현재 가장 빨리 끝나는 강의와 비교하여 강의실 재사용 여부 판단
      heapq.heappop(min_heap)   # 기존 강의실 재사용 가능하면 제거

    heapq.heappush(min_heap, end)

  return len(min_heap)

n = int(input())
lec = [tuple(map(int,input().split())) for _ in range(n)]
print(classroom(n, lec))
