def solution(n, lost, reserve):
    # lost랑 reserve 안 겹치는 사람들 (중복 제거)
    real_lost = [l for l in lost if l not in reserve] # 여벌도 없고 도난 당함
    real_reserve = [r for r in reserve if r not in lost] 
    
    # 정렬 (안해주면 뒷 사람거를 앞 사람에게 빌려줘버려서 뒤에 있는 학생이 못 빌리는 경우 발생)
    real_lost.sort()
    real_reserve.sort()
    
    # 빌려주기
    for r in real_reserve :
        if r-1 in real_lost :
            real_lost.remove(r-1)
        elif r+1 in real_lost :
            real_lost.remove(r+1)
    
    return n-len(real_lost)