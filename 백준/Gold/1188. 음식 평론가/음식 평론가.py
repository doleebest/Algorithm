# 최대 공약수 구하기
def func(N,M) :
    while M != 0:
        remainder = N%M
        N = M
        M = remainder
    return N

N,M = map(int, input().split())
original_M = M # 원래 m이 훼손되므로 이걸 따로 저장함
f = func(N,M)
print(original_M-f)