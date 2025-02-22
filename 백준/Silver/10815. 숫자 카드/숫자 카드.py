import sys
m = int(sys.stdin.readline().strip()) 
sk = list(map(int, sys.stdin.readline().split()))
n = int(sys.stdin.readline().strip()) 
card = list(map(int, sys.stdin.readline().split()))

sk.sort()

def binary_search(target, data) :
  start= 0
  end = len(data)-1

  while start<=end :
    mid = (start+end) // 2    # 중간값
    if data[mid] == target :
      return 1
    elif data[mid]>target :
      end = mid-1
    else : start = mid+1
  return 0

for i in range(0,n) :
    card[i] = binary_search(card[i],sk)

print(*card)