a,b = map(int,input().split())
def gcd (a, b) :
    while(b) :
        a %= b
        a,b = b,a
    return a

def lcm (a,b) :
    return int(a*b/gcd(a,b))

print(gcd(a,b))
print(lcm(a,b))
