target = int(input())
ans = abs(100-target)
m = int(input())

if m : # 고장난 버튼이 있는 경우에만 고장난 버튼들의 list를 받음
  broken = set(input().split())
else:
  broken = set()

# 고장난 버튼을 피해 가장 가까운 숫자 찾기
for num in range(1000001) :
  for N in str(num) : # num 각 자리 숫자가 고장났는지 확인. 즉 고장 안 난 숫자를 찾아가는 과정
    if N in broken : # 고장난 버튼이 포함되면 사용 불가능하므로 넘어감(break)
      break
  else : # 번호를 눌러서 만들 수 있는 경우엔
      # min(기존답, 번호를 누른 횟수 + 해당 번호로부터 타켓까지의 차이)
      ans = min(ans, len(str(num))+abs(num-target))

print(ans)
