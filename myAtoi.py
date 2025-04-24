def myAtoi(s: str) -> int:
    if len(s) == 0 or s.lstrip() == '':
        return 0
    
    s = s.lstrip()

    if s[0] == '-':
        sign = -1
        s = s[1:]
    elif s[0] == '+':
        sign = 1
        s = s[1:]
    else:
        sign = 1

    s = s.lstrip('0')
    k = ''
    if sign < 0:
        for i in s:
            if i.isdecimal():
                k += i
            else:
                break
        if k != '':
            if int(k) * sign < -2**31:
                return -2**31
            else:
                int(k) * sign
        else:
            return 0
    else:
        for i in s:
            if i.isdecimal():
                k += i
            else:
                break
        if k != '':
            if int(k) * sign > 2**31 - 1:
                return 2**31 - 1
            else:
                int(k) * sign
        else:
            return 0

        
print(myAtoi(' '))
        