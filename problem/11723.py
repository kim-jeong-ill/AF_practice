#집합

M = int(input())
S = []

for _ in range(M):
    x = input()
    if x == 'all':
        S = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    elif x == 'empty':
        S = []
    else:
        x.split(' ')
        sen = x[0]
        num = x[1]
        if sen == 'add':
            if num in S:
                continue
            else:
                S.append(num)
        elif sen == 'remove':
            if num in S:
                S.remove(num)
            else:
                continue
        elif sen == 'check':
            if num in S:
                print(1)
            else:
                print(0)
        elif sen == 'toggle':
            if num in S:
                S.remove(num)
            else:
                S.append(num)
    