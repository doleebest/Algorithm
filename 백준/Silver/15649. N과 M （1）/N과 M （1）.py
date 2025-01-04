from itertools import permutations
import sys
n,m = map(int, sys.stdin.readline().split())
arr = [i+1 for i in range (n)]
result = permutations(arr,m)
for seq in result:
    print(*seq)
    