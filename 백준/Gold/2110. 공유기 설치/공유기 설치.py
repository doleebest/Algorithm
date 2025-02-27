n, c = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

array.sort()

def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2 	# 현재 공유기 거리.
        current = array[0] 		 	# 첫 집에 공유기 설치
        count = 1

        for i in range(1, len(array)):
            if array[i] >= current + mid: # 이전 공유기 위치 + mid 
                count += 1
                current = array[i]

        if count >= c:		# 너무 많이 설치됐으면
            global answer
            start = mid + 1 # 공유기 사이 거리 늘림
            answer = mid
        else:
            end = mid - 1	# 공유기 설치 수가 목표 보다 작으면 공유기 사이 거리 줄임


start = 1 # 공유기 거리 최소 
end = array[-1] - array[0] # 공유기 거리 최대
answer = 0

binary_search(array, start, end)
print(answer)