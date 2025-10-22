N,M = map(int, input().split())
du = set()
bo = set()
for i in range(N) :
    du.add(input().strip())
for j in range(M) :
    bo.add(input().strip())

answer=[]
for d in du :
    if d in bo :
        answer.append(d)
answer.sort()
print(len(answer))
for l in answer :
    print(l)