import sys
import heapq as hq
n = int(sys.stdin.readline())
heap = []
for i in range(n) :
    x = int(sys.stdin.readline())*(-1)
    if x==0 : print(hq.heappop(heap)*(-1) if heap else 0)
    else:     
        hq.heappush(heap,x)