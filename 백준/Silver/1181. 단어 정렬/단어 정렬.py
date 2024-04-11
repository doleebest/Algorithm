import sys
n = int(sys.stdin.readline())
arr = [(sys.stdin.readline()).strip() for _ in range(n)]
arr = set(arr)
arr = list(arr)
arr.sort()
arr.sort(key = len)
for i in arr:
    print(i)