n = int(input())
for i in range(n) :
    a = input()
    score = 0
    sumScore = 0 
    for char in a:
        if char == 'O' :
           score += 1
        else :
            score = 0
        sumScore += score
    print(sumScore)