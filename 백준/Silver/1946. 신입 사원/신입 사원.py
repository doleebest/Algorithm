import sys
T = int(sys.stdin.readline())
for _ in range(T) :
    N = int(sys.stdin.readline())
    rank = sorted([list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)])
    cnt = 1
    max = rank[0][1]
    for i in range(N) :
        if rank[i][1] < max :
            max = rank[i][1]
            cnt+=1
    print(cnt)