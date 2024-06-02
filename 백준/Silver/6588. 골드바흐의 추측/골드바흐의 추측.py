import sys
aris = [True] * 1000001
aris[0], aris[1] = False, False
for i in range(2, 1001) :
    if aris[i] :
        for j in range(i*i,1000001,i) :
            aris[j] = False
while (1):
    n = int(sys.stdin.readline())
    if n == 0 :
        break
    for i in range(3,n,2) :
        if aris[i] and aris[n-i] :
            print(f"{n} = {i} + {n-i}")
            break
    else : print("Goldbach's conjecture is wrong.")