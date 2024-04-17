import itertools
import random
n = 9
arr = [int(input()) for _ in range(n)]
nCr = itertools.combinations(arr,7)
whole = list(nCr)
answer = []
for tpl in whole :
    if sum(tpl)== 100 : answer.append(tpl)
choicelist = (list(random.choice(answer)))
choicelist.sort()
for i in choicelist :    
    print(i)