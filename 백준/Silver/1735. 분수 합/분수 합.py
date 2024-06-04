a,b = map(int,input().split()) # a/b
c,d = map(int,input().split()) # c/d

son = (b*c+a*d)
mom = b*d
def gcd(a,b):
    while(b) :
        a%=b
        a,b = b,a
    return a
x = gcd(mom,son)
print(int(son/x),int(mom/x))