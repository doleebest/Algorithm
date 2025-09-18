n = int(input())
a = list(map(int,input().split()))
b,c = map(int,input().split())

ans = 0
ans += len(a) # 총 감독관

left = a
for i in range(len(left)) :
    left[i] = left[i]-b # 총감독관 빼면 몇명 남았는지

for i in range(len(left)) :
    if left[i]>0 :
        ans+=(left[i]+(c-1)) // c

print(ans)