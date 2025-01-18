import sys

def dfs(n,tlst) :
    if n==M : # 종료조건
        ans.append(tlst)
        return
    
    prev = 0 # 중복 안하기 위해서 설정한 값
    for j in range(N) : # 주어진 리스트에서 
        if v[j] == 0 and prev != lst[j] : 
            # 숫자가 이미 사용했는가? + 중복 확인
            prev = lst[j] # 이전 숫자와 같지 않은 경우만 선택해서 중복 방지
            v[j]=1
            dfs(n+1, tlst+[lst[j]])
            v[j] =0
            
N,M = map(int, input().split())
lst = sorted(list(map(int, input().split())))

ans = []
v = [0]*N
dfs(0,[])

for lst in ans :
    print(*lst)