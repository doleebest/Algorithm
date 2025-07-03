n = int(input())
A = list(map(int, input().split()))

# 1. L[i] 계산 (왼쪽에서부터 최대 연속합, i 포함)
L = [0] * n
L[0] = A[0]
for i in range(1, n):
    L[i] = max(A[i], L[i-1] + A[i])

# 2. R[i] 계산 (오른쪽에서부터 최대 연속합, i 포함)
R = [0] * n
R[-1] = A[-1]
for i in range(n-2, -1, -1):
    R[i] = max(A[i], R[i+1] + A[i])

# 3. 제거하지 않았을 때 최대 연속합
answer = max(L)

# 4. 하나 제거했을 때의 최댓값도 고려
for i in range(1, n - 1):
    answer = max(answer, L[i-1] + R[i+1])

print(answer)