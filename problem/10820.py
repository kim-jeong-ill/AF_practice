#문자열 분석

while 1:
    try:
        n = input()
        if n == "":
            break
        else:
            n = list(str(n))
            u = 0
            l = 0
            num = 0
            blank = 0
            for i in n:
                if ord(i) >= 65 and ord(i) <= 90:
                    u += 1
                elif ord(i) >= 97 and ord(i) <= 122:
                    l += 1
                elif ord(i) >= 48 and ord(i) <= 57:
                    num += 1
                else:
                    blank += 1

            print(l, u, num, blank)
    except EOFError:
        break