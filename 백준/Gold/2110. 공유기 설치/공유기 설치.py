n,c = map(int,input().split())
home = []
for i in range(n) :
    home.append(int(input()))
    
home.sort()

def binary_search(home, start, end) :
    while start<=end : 
        mid = (start+end)//2
        count = 1
        current = home[0]
        
        for i in range(1,len(home)) :
            if home[i] >= current+mid :
                count+=1
                current = home[i]
        
        if count>=c :
            global answer
            start = mid+1
            answer = mid
        else :
            end = mid-1

start = 1
end = home[-1]-home[0]
answer = 0
binary_search(home,start,end)
print(answer)