#8진수 2진수

n = input()
n = list(n)
n = list(map(int, n))
l = []

for i in n:
    temp = []
    while 1:
        share = i // 2
        rest = i % 2
        temp.append(rest)
        if share <= 0:
            break
        i = share
    temp.reverse()
    if len(temp) == 1:
        temp.insert(0, 0)
        temp.insert(0, 0)
    elif len(temp) == 2:
        temp.insert(0, 0)
    for j in temp:
        l.append(j)

k = 0
if len(l) == 3:
    if l[0] == 0 and l[1] == 0 and l[2] == 0:
        print(0)
else:
    while 1:
        if l[k] == 0:
            l.remove(k)
        else:
            break

    for x in l:
        print(x, end='')