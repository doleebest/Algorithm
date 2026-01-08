# L보다 크거나 같고, R보다 작거나 같은 자연수 중에 
# 8이 가장 적게 들어있는 수에 
# 들어있는 8의 개수

# 자릿수를 고정해서 보는가?
# 그럼 어디부터 고정해서 보는가?
# 앞에서부터 봐야한다고 생각. 왜냐하면 그러면 뒤에는 자유로우니까

A, B = map(str, input().split(' '))

ret = 0

if len(A) != len(B):
    print(0)

else: 
    for i in range(len(A)):
        if A[i] == B[i]:
            if A[i] == '8':
                ret += 1
        else:
            break
    print(ret)
