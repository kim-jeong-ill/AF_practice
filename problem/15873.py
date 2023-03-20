#공백 없는 A+B

n = list(str(input()))

n = list(map(int, n))

if len(n) <= 2:
    print(n[0] + n[1])
    
else:
    if len(n) == 4:
        print(20)
    else:
        if n[1] == 0:
            print(10 + n[2])
        else:
            print(n[0] + 10)