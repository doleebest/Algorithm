n = int(input())
arr= list(map(int, input().split()))

for i in range(n-1, 0, -1) :
    if arr[i-1] < arr[i] :
        for j in range(n-1, 0 ,-1) :
            if arr[j] > arr[i-1] :
                arr[i-1], arr[j] = arr[j], arr[i-1]
                arr = arr[:i] + sorted(arr[i:]) # :i는 i 미포함.
                for i in arr :
                    print(i ,end=' ')
                exit()

print(-1)