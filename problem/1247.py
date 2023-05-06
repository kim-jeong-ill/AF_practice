#부호


for _ in range(3):
    n = int(input())
    l = []
    for _ in range(n):
        s = int(input())
        l.append(s)
    if sum(l) < 0:
        print('-')
    elif sum(l) == 0:
        print(0)
    else:
        print('+')