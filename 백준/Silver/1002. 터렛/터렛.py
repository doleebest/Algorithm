import math

t = int(input()) # 케이스 개수

for i in range (t) :
    x1,y1,r1, x2,y2,r2 = map(int, input().split()) # 값 반환 받기
    distance = math.sqrt((x2-x1)**2+(y2-y1)**2) # 두 원의 거리

    if (x1==x2) and (y1==y2):
        if(r1==r2) : print(-1)
        else : print(0)
    else:
        if(distance==r1+r2) or abs(r1-r2)==distance: print(1)
        elif(distance>r1+r2) or abs(r1-r2)>distance: print(0) 
        elif r1+r2 > distance > abs(r1-r2) : print(2)