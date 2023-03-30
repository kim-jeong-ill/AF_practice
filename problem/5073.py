#삼각형과 세 변

while 1:
    a,b,c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    else:
        l = []
        l.append(a)
        l.append(b)
        l.append(c)
        l.sort()
        if l[0] + l[1] >= l[2]:
            if l[0] == l[1] and l[1] == l[2]:
                print('Equilateral')
            elif l[0] == l[1] or l[0] == l[2]:
                print('Isosceles')
            else:
                print('Scalene')
        else:
            print('Invalid')
        