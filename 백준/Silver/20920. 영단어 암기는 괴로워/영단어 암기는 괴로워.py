# 순위 적용
# 1. 자주 나오는 단어일수록 앞에 배치한다.
# 2. 해당 단어의 길이가 길수록 앞에 배치한다.
# 3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다

import sys
# 지문에 있는 단어들을 받는다.
N,M = map(int,sys.stdin.readline().split())
d = dict()
for i in range(N):
    # 길이가 M 이상인 단어들이고
    word = sys.stdin.readline().strip()
    if len(word) >= M :
        if word not in d :
            d[word]= 1
        else:
            d[word] +=1

dic = sorted(d.items(), key= lambda x : (-x[1], -len(x[0]), x[0]))

for k,v in dic :
    print(k)
