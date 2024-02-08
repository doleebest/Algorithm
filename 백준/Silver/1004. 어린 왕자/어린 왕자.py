t = int(input()) # 테스트 케이스 횟수

for _ in range(t) : 
    x1, y1, x2, y2 = list(map(int,input().split())) #출발점, 도착점
    
    count = 0 # 진입 및 이탈 횟수
    planet = int(input()) # 행성계의 개수
    for _ in range(planet) :
        cx, cy, r = map(int,input().split()) # 행성계의 중심과 반지름
        
        dis1 = (x1-cx)**2 + (y1-cy)**2
        dis2 = (x2-cx)**2 + (y2-cy)**2
        pow_cr = r**2

        if pow_cr > dis1 and pow_cr>dis2 : 
            pass
        elif pow_cr > dis1 : 
            count+=1
        elif pow_cr > dis2 : 
            count +=1

    print(count)

