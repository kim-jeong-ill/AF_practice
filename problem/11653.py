#소인수분해

n = int(input())

if n == 1:
    print()
else:
    l = []
    i = 2
    while 1:
        if n % i == 0:
            l.append(i)
            n = n // i
            i = 2
        else:
            i += 1
            
        if n == 1:
            break
            
    for i in l:
        print(i)