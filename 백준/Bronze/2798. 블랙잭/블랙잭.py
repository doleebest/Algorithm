N,M = map(int,input().split())
cards = list(map(int,input().split()))
ans = 0

for i in range(0,N) :
    for j in range(i+1,N) :
        for k in range(j+1,N) :
            sum3 = cards[i]+cards[j]+cards[k]
            if sum3 <= M :
                ans = max(ans,sum3)

print(ans)