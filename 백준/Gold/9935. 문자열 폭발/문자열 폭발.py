import sys
arr= sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()

stack = []

for i in range(len(arr)) :
  stack.append(arr[i])
  if ''.join(stack[-len(bomb):]) == bomb : # stack의 마지막 len(bomb)개의 문자를 잘라서 리스트로 가져온다.
    for _ in range(len(bomb)) :
      stack.pop()

if stack : 
  print(''.join(stack))
else :
  print('FRULA')
