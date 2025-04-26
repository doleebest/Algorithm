def cut(start, end):
    result = 0  # 가장 긴 랜선 길이를 저장할 변수
    while start <= end:
        mid = (start + end) // 2
        
        count = 0
        for length in lines:
            count += length // mid

        if count >= N:  # 만들 수 있으면 길이를 더 늘려본다
            result = mid  # 일단 저장
            start = mid + 1
        else:  # 만들 수 없으면 길이를 줄인다
            end = mid - 1

    return result

K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

start = 1
end = max(lines)
answer = cut(start, end)
print(answer)
