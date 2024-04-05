def hanoi(num,a,b,c) : 
    if num==1:
        print(a,c)
    else :
        hanoi(num-1,a,c,b) # a->b
        hanoi(1, a,b,c) # 하나만 a ->c
        hanoi(num-1, b,a,c) # b->c
 
n = int(input())   
print(2**n-1)
if(n<=20):
    hanoi(n,1,2,3)