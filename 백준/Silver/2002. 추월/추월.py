import sys
n= int(sys.stdin.readline())
in_car = {}
cnt=0
for i in range(n) :
    in_car[input()] = i
out_car = [str(input()) for _ in range(n)]

for i in range(n-1) :
    for j in range(i+1,n) :
        if in_car[out_car[i]] > in_car[out_car[j]] :
            cnt+=1
            break
print(cnt)