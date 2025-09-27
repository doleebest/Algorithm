import sys
# 문자열의 길이가 100을 넘지 않으므로 그냥 다 for 문 돌려가면서 
for line in sys.stdin : # N번 반복하면서 문자열 받고 체크하고 정답 프린트
    line = line.rstrip("\n")
    d = 0
    l = 0
    u = 0
    s = 0
    for j in range(len(line)) :
        if line[j].isdigit() : d+=1
        elif line[j].islower() : l+=1
        elif line[j].isupper() : u+=1
        elif line[j].isspace() : s+=1
    print(l,u,d,s)