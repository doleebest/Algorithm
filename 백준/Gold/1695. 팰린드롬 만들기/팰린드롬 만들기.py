def min_insertions_to_palindrome(A):
    N = len(A)
    dp = [0] * N  # 1차원 DP 배열

    # 뒤에서 앞으로 구간 길이를 늘리며 계산
    for start in range(N - 2, -1, -1):  # 시작점
        prev = 0  # 이전 dp[j-1] 값을 저장
        for end in range(start + 1, N):  # 끝점
            temp = dp[end]  # 현재 dp[end] 값을 저장
            if A[start] == A[end]:
                dp[end] = prev  # 같으면 이전 구간 그대로 사용
            else:
                dp[end] = min(dp[end], dp[end - 1]) + 1  # 다르면 삽입 최소값 계산
            prev = temp  # 현재 값을 다음 루프에서 이전 값으로 사용

    return dp[N - 1]  # 전체 구간의 최소 삽입 횟수

# 입력
N = int(input())
A = list(map(int, input().split()))

# 결과 출력
print(min_insertions_to_palindrome(A))
