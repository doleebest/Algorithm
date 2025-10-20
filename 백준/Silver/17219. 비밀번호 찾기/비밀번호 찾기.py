# 사이트 주소 갯수, 비밀번호 찾으려는 사이트 주소의 수 받고
n,m = map(int,input().split())
# 사이트 주소와 비밀번호를 받아서 사전에 저장
book = dict()
for i in range(n) :
    a,b = input().split(" ")
    book[a] = b

# 비번을 뱉어내야함
for j in range(m) :
    site = input().strip()
    print(book[site])