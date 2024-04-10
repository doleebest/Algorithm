import sys
data = [int(sys.stdin.readline()) for __ in range(int(sys.stdin.readline()))]
data.sort()
for i in data:
    print(i)