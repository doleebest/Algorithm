# 주어진 수의 순서를 바꾸면 안 된다.
# 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다. 
# 또, 나눗셈은 정수 나눗셈으로 몫만 취한다. 
# 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다.

def dfs(n, sm, add, sub, mul, div) :
    global mn, mx
    # 결과값/ 중간값의 범위는 nt(1e8), int(-1e8) 사이
    # 그 범위 벗어나면 더 이상 할 필요가 없음
    if sm <-int(1e9) or sm>int(1e9) :
        return
    
    # 종료 조건 = 정답 처리
    if n == N :
        mn = min(mn,sm)
        mx = max(mx,sm)
        return

    # 하부 호출 : 연산자 개수 남았을 경우만 호출 가능
    if add > 0 :
        dfs(n+1, sm+lst[n], add-1,sub,mul,div)
    if sub > 0 :
        dfs(n+1, sm-lst[n], add,sub-1,mul,div)
    if mul > 0 :
        dfs(n+1, sm*lst[n], add,sub,mul-1,div)
    if div > 0 :
        dfs(n+1, int(sm/lst[n]), add,sub,mul,div-1)
        
N = int(input())
lst = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

mn, mx = int(1e9), int(-1e9)
dfs(1, lst[0], add, sub, mul, div)
print(mx, mn, sep='\n')