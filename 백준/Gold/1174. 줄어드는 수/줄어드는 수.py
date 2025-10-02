ans = []
def dfs(jaritsu,n,k,num) :
    # 종료 조건
    if n == jaritsu:
        ans.append(int("".join(map(str, num))))
        return

    # 첫째 자리수가 0이면 안됨
    for i in range(k) :
        dfs(jaritsu,n+1,i,num+[i])


N = int(input())

# 시작을 어디서부터 하지?
for j in range(1,11) :
    for i in range(10) :
        if j > 1 and i == 0:  # 다자리 수에서 선행 0 방지
            continue
        dfs(j,1, i,[i])

ans.sort()
if N> len(ans) :
    print(-1)
else :
    print(ans[N-1])