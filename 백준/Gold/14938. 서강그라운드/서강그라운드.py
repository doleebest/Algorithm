import sys
n,m,r = map(int, sys.stdin.readline().split())
items = [0] + list(map(int,input().split()))
vertex = [[sys.maxsize for j in range(n+1)] for i in range(n+1)]
for i in range(n+1) : vertex[i][i]=0
for i in range(r) :
    a,b,dist = map(int,sys.stdin.readline().split())
    vertex[a][b] = dist
    vertex[b][a] = dist

for k in range(n+1) :
    for i in range(n+1) :
        for j in range(n+1) :
            if vertex[i][j] > vertex[i][k] + vertex[k][j] :
                vertex[i][j] =vertex[i][k] + vertex[k][j]

answer = 0
for i in range(1,n+1) : 
    can_get_item = [items[x] for x in range(1,n+1) if vertex[i][x] <= m]
    answer = max(answer,sum(can_get_item))
    
print(answer)