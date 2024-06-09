import math
import sys
n = int(sys.stdin.readline())
for _ in range(n) :
    result = 0
    arr = list(map(int,input().split()))
    for i in range(1,len(arr)) :
        for j in range(i+1,len(arr)) :
            result += math.gcd(arr[i],arr[j])
    print(result)