import sys
n1 = int(sys.stdin.readline())
for _ in range(n1) :
    clth = {}
    result = 1
    n2 = int(sys.stdin.readline())
    for _ in range(n2) :
        name, type = sys.stdin.readline().strip().split()
        if not type in clth :
            clth[type] = 1
        else : 
            clth[type] +=1
    for i in clth:
        result *= (clth[i] +1)
    print(result-1)  