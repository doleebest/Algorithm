n = int(input())
for _ in range(n) :
    score_list = list(map(int,input().split()))
    stdnt = 0
    # calculate avg
    avg = sum(score_list[1:])/score_list[0]
    
    for i in score_list[1:]:
        if i > avg :
            stdnt += 1
    result = round(stdnt*100/(len(score_list)-1),3)
    
    print(f"{result}%")
