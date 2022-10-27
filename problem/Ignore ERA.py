#가희와 방어율 무시

a, b = map(int, input().split())


if b == 0:
    if a <= 100:
        print(1)
else:
    if (a / 100 * (100-b))  < 100:
        print(1)
    else:
        print(0)