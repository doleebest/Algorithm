n = int(input().strip())
cards = list(map(int,input().split()))      # 갖고 있는 카드
m = int(input().strip())
candidate = list(map(int,input().split()))   # 상근이가 물어볼 카드 번호

# cards 리스트에 있는 각 숫자의 개수를 세서 딕셔너리에 저장
count = dict()
for c in cards:
    if c in count :
        count[c]+=1
    else :
        count[c] = 1

# 물어본 숫자들에 대해서만 개수 출력
# value 출력
for target in candidate:
    result = count.get(target)
    if result is None :
        print(0, end= " ")
    else :
        print(result, end=" ")

