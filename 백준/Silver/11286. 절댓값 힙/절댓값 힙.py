import heapq, sys
heap = []
n = int(sys.stdin.readline())
for _ in range(n) : 
    x = int(sys.stdin.readline())  
    if x : 
        heapq.heappush(heap,(abs(x),x)) # 만약 x가 0이 아니라면 배열에 x라는 값을 넣는(추가하는) 연산이고, 
    else: 
        if heap : print(heapq.heappop(heap)[1]) 
        else : print(0)