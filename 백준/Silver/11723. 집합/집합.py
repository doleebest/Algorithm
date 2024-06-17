import sys
n= int(sys.stdin.readline())
s = set()

for _ in range(n) :
    temp = sys.stdin.readline().strip().split()
    if len(temp) == 1 :
        if temp[0] == "all" : s = set([i for i in range(1,21)])
        else : s = set()
    else :    
        cal = temp[0]
        x = int(temp[1])
        if cal == "add" : s.add(x)
        elif cal == "remove" : s.discard(x)
        elif cal == "check" : print(1 if x in s else 0)
        elif cal == "toggle" : 
            if x in s : s.discard(x)
            else : s.add(x)
