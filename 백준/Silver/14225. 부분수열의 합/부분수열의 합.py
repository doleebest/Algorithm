n = int(input())
arr = list(map(int, input().split()))

arr.sort()
target = 1  # 만들 수 있는 최소 자연수 초기값

for num in arr:
    if num > target:  # 만들 수 없는 경우 발견!
        break
    target += num  # 만들 수 있으면 target 늘리기

print(target)
