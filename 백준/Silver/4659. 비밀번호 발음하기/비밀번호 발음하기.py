import sys
vowel = ["a","e","i","o","u"]
for line in sys.stdin :
    acceptable = False
    password = list(line.strip())
    if ''.join(password) == 'end' :
        break

    # 조건1.
    rule_1 = any(v in password for v in vowel)  # 조건 1

    # 조건2.
    rule_2 = True
    for i in range(len(password)-2) :
            if (password[i] in vowel and password[i+1] in vowel and password[i+2] in vowel) or (password[i] not in vowel and password[i+1] not in vowel and password[i+2] not in vowel): # 조건2
                rule_2 = False

    # 조건3.
    rule_3 = True
    for i in range(len(password)-1) :
        if password[i] == password[i+1] :
            if (password[i]=='e' or password[i]=='o') :  # 조건3
                rule_3 = True
            else:
                rule_3 = False

    # 결과값 프린트
    if rule_1 == 1 and rule_2 == 1 and rule_3==1 :
        print(f"<{''.join(password)}> is acceptable.")
    else :
        print(f"<{''.join(password)}> is not acceptable.")