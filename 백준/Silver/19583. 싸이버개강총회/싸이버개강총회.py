import sys
# 입력
# 시작시간, 끝낸 시간, 스트리밍 끝낸 시간
s,e,q = map(str,input().split())
s = s.replace(":","")
e = e.replace(":","")
q = q.replace(":","")

attend= set()
cnt = 0
for line in sys.stdin:
    time, name = line.strip().split()
    time = time.replace(":","")
    if time<=s :
        attend.add(name)
    elif e<=time<=q and name in attend :
        attend.remove(name)
        cnt+=1

print(cnt)

