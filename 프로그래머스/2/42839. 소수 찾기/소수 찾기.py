# 소수의 조건 : 약수가 1과 자기 자신
# 2부터 n-1까지 나눠보고 만약 나머지가 0이 아니면 b=1
# b=0 이면 소수이고 아니면 소수 아님
import itertools

def isPrime(n) :
    for i in range(2,n) :
        if n%i == 0 :
            return False
    return True # for문이 다 끝나고 나면 return
    
def solution(numbers):
    # 1. 문자열을 한 글자씩 잘라서 숫자로 다 분리
    arr = list(map(int, list(numbers)))
    
    # 2. 순열을 구한다.
    all = []
    for i in range(1,len(arr)+1) :
        all += list(itertools.permutations(arr,i))
    
    # 3. 숫자로 변환
    temp = []
    for elem in all :
        number = 0
        for i in range(len(elem)) :
            number+= 10**(len(elem)-1-i)*elem[i]
        temp.append(number)
    
    # 4. 중복되는 숫자 제거
    temp = list(set(temp))
    
    # 5. 소수로 구성된 리스트를 만듦
    answer = []
    for t in temp :
        if t>1 and isPrime(t) :
            answer.append(t)

    return len(answer)