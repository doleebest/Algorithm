import sys
n = int(sys.stdin.readline())
enter = dict()
for _ in range(n):
    name, status = map(str, sys.stdin.readline().split())    
    if status == "enter" : enter[name] = status
    else : del enter[name]
enter = sorted(enter.keys(), reverse=True)
for i in enter :
    print(i) 