n = int(input())

def attack(x) :
    for i in range(x) :
        if row[x]==row[i] or abs(row[x]-row[i]) == abs(x-i):
            return True
    return False

def queen(x) :
    global cnt
    if x == n :
        cnt +=1 
    else :
        for i in range(n) :
            row[x] = i
            if not attack(x):
                queen(x+1)

row= [0]*n
cnt = 0
queen(0)
print(cnt)