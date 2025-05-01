def solution(n, times):
    left = 1
    max_time = max(times)
    right = n*max_time
    
    while left <= right :
        mid = (left+right) // 2
        people = 0 
        for t in times : 
            people += mid//t #중간에라도 넘 많이 심사하면 멈춤
            if people >= n : break
        
        # n명 초과 심사 -> 시간이 넉넉
        if people >= n :
            answer = mid
            right = mid-1
        # n명 미만 심사 -> 시간이 부족
        else :
            left = mid+1
    return answer