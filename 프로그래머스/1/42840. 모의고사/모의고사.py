# 1번 수포자 = [1,2,3,4,5]
# 2번 수포자 = [2,1,2,3,4,5]
# 3번 수포자 = [3,3,1,1,2,2,4,4,5,5]

def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    cnt = [0,0,0]
    answer = []
    for i in range(len(answers)) :
        if answers[i] == one[i%5] : cnt[0] += 1
        if answers[i] == two[i%8] : cnt[1] += 1
        if answers[i] == three[i%10] : cnt[2] += 1
    
    for idx, value in enumerate(cnt) :
        if value == max(cnt) : answer.append(idx + 1)
            
    return answer