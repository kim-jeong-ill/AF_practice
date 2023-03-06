#Median
i=1

while 1:
    n = list(map(int, input().split()))
    if len(n) == 1 and n[0] == 0:
        break
    n.sort()
    n.reverse()
    if len(n) % 2 == 0:
        tmp = len(n) // 2 - 1
        print('Case', i, end='')
        print(': ', end='')
        print((n[tmp] + n[tmp+1])/2)
    elif len(n) % 2 == 1:
        tmp = len(n) // 2
        print('Case', i, end='')
        print(': ', end='')
        print(n[tmp]/1)
    i += 1