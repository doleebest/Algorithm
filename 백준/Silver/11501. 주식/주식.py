import sys
t = int(sys.stdin.readline())
interest = 0 
for _ in range(t) :
    n = int(sys.stdin.readline())
    price = list(map(int,sys.stdin.readline().split()))
    interest = 0
    max = 0
    for i in range(len(price)-1,-1,-1) :
        if max < price[i] :
            max = price[i] 
        else : # 현재 가격이 현재 최대 가격보다 작다면 차익 실현
            interest += max - price[i]
    print(interest)