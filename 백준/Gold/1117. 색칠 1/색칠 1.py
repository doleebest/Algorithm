import sys
input = sys.stdin.readline

# 1억 x 1억이라 이차원 배열을 그리는건 무리라고 판단.
W, H, f, c, x1, y1, x2, y2 = map(int, input().split())

# 중첩되는 구간과 중첩되지 않는 구간이 생긴다.
# 중첩된 맨 오른쪽 좌표는 W-f, f 중 작은 좌표가 된다.
boundary = min(W-f, f)

if x1 <= boundary <= x2:
    k = 2 * (boundary-x1) + (x2-boundary)
elif boundary <= x1:
    k = (x2-x1)
else: # x2 <= boundary:
    k = 2 * (x2-x1)
    
# c+1 개가 겹치니깐 c+1 배가 된다.
print(W*H - k * (c+1) * (y2-y1))