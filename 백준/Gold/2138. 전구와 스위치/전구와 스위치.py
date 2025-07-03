def toggle(arr, i):
    for j in [i-1, i, i+1]:
        if 0 <= j < len(arr):   # 범위 내에 있으면
            arr[j] = 1 - arr[j] # flip

def simulate(a, b, press_first):
    n = len(a)
    cnt = 0
    arr = a[:]

    if press_first:     # 1번 스위치를 누른 상태로 시작할 건지 여부를 결정하는 boolean 변수
        toggle(arr, 0)  # 1번 스위치를 누르기로 했으면 눌러서 flip
        cnt += 1        # 누른 횟수 증가

    for i in range(1, n):       # 일치하지 않으면 또 flip
        if arr[i-1] != b[i-1]:
            toggle(arr, i)
            cnt += 1

    if arr == b:         # 같으면 이제 반환 가능
        return cnt
    else:
        return float('inf')

n = int(input())
a = list(map(int, input().strip()))
b = list(map(int, input().strip()))

res = min(simulate(a, b, True), simulate(a, b, False)) # 1번 스위치를 누를 수도 있고, 안 누를 수도 있고. 그 중 적게 누른거 
print(res if res != float('inf') else -1)
