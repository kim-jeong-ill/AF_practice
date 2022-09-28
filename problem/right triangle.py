while 1:
    a = input().split(' ')
    a = list(map(int, a))
    a.sort()
    if a[0] == 0 and a[1] == 0 and a[2] == 0:
        break
    if a[2]*a[2] == a[1]*a[1] + a[0]*a[0]:
        print('right')
    else:
        print('wrong')
