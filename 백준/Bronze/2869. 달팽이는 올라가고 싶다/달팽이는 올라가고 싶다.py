import math
A, B, V = map(int,input().split())

# 달팽이가 목표 높이에 닿으면 다시 미끄러질 일이 없다.
x = math.ceil((V-A)/(A-B)+1)
print(x)