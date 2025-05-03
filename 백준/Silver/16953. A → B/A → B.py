a,b = map(int,input().split())
r=1
while(b!=a) :
    r+=1
    temp = b
    if b%10 == 1 : b//=10 # 끝에 1이 존재한다면 끝의 1을 빼기
    elif b%2 ==0 : b//=2 # 짝수인 경우에만 2로 나누기
    
    if temp==b : # 연산을 수행했지만 값의 변화가 없는경우, 무한루프
        print(-1)
        break
else : print(r)