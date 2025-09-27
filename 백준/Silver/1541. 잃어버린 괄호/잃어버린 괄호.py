# - 을 기준으로 다 split ["10", "20+30", "40+50"]
# 각 요소별로 +로 다 split ["10", ["20", "30"], ["40","50"]]
# 각 요소별로 int로 바꾼 다음에, 다 더하기
# 그리고 [0]번 요소에서 1~끝까지 해서 차례로 빼주기

line = input()
line_num = line.split("-")
for i in range(len(line_num)) :
    line_num[i] = line_num[i].split("+")

for j in range(len(line_num)) :
    for k in range(len(line_num[j])) :
        line_num[j][k] = int(line_num[j][k])

for l in range(len(line_num)) :
    line_num[l] = sum(line_num[l])

init = line_num[0]
for m in range(1,len(line_num)) :
    init-=line_num[m]
print(init)