x = input() # 문자열로 반환
if type(x) == int:
    print(chr(x))
elif type(x) == str:
    print(ord(x))