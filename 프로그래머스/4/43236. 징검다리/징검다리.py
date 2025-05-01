def solution(distance, rocks, n):
    rocks.sort()
    left = 1
    right = distance
    answer = 0
    
    while left <= right : 
        mid = (left+right)//2 # 최소 거리 후보
        prev = 0 # 이전 바위의 위치
        removed = 0 # 제거한 바위의 개수
        
        # 바위 사이의 간격이 13 이상 되도록 하고 싶음
        for r in rocks :
            if r-prev < mid : # 13보다 작음 너무 가까움
                removed += 1 # 제거
            else : # 13보다 크면
                prev = r # 
        
        # 도착 지점과의 거리 측정
        if distance - prev < mid :
            removed += 1
        
        if removed > n :
            right = mid -1
        else :
            answer = mid
            left = mid+1
                
    return answer