# 1부터 n개의 번호가 붙어있는 포도주들
# 가장 많은 양의 포도주 시식할 수 있도록
# n 포도주 잔의 수
# 연속으로 있는 3개의 잔은 못 마심. 그럼 1,2개는 마실 수 있다는 거네
# dp?

n=int(input())
wine=[0]*10000
for i in range(n):
  wine[i]=int(input())

# n-2 전까지의 최대양 + 현재양
# 전전전(n-2)까지의 최대 양 + 전(n-1)양 + 현재 양
d=[0]*10000
d[0] = wine[0]
d[1] = wine[0]+wine[1]
d[2] = max(wine[2]+wine[0], wine[2]+wine[1], d[1])
for i in range(3,n) :
    d[i] = max(wine[i]+d[i-2], wine[i]+wine[i-1]+d[i-3], d[i-1])
print(max(d))