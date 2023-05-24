def check_rule_1(str):
    return len(str) > 8

def check_rule_2(str):
    case = 0
    CASE = 0
    num = 0
    other = 0
    for ch in str:
        if case + CASE + num + other >= 3:
            return True
        asc = ord(ch)
        if asc >= 97 and asc <= 122:
            case = 1
        elif asc >= 65 and asc <= 90:
            CASE = 1
        elif asc >= 48 and asc <= 57:
            num = 1
        elif asc != 32 and asc != 10:
            other = 1
    return case + CASE + num + other >= 3

def check_rule_3(str):
    for i in range(len(str) - 3):
        if len(s.split(s[i:i+3])) >= 3:
            return False
    return True

while True:
    try:
        s = str(input())

        res = ''
        if check_rule_1(s) and check_rule_2(s) and check_rule_3(s):
            print('OK')
        else:
            print('NG')
    except:
        break


