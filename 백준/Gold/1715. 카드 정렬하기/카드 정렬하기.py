import heapq

n = int(input())
arr = []
for _ in range(n) : 
  heapq.heappush(arr, int(input()))

total = 0
while len(arr) > 1 :
  num1 = heapq.heappop(arr)
  num2 = heapq.heappop(arr)
  sum = num1+num2

  total+=sum
  heapq.heappush(arr, sum)

print(total)