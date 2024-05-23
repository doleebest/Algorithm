import sys
n,m = map(int,sys.stdin.readline().split())
pocketmons = {}
reverse = {}
for i in range(1,n+1) :
    mon = sys.stdin.readline().strip()
    pocketmons[mon] = i
    reverse[i] = mon

for _ in range(m):
    q = sys.stdin.readline().strip()
    if q.isdecimal() :
        print(reverse[int(q)])
    else :
        print(pocketmons[q])