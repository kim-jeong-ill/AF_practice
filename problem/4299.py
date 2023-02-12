#AFC 윔블던

a,b = map(int, input().split())

# x + y = a , x - y = b
# a+b = 2x
if a - b < 0 or (a+b)%2 != 0:
    print(-1)

else:
    x = (a+b)//2
    y = a - x

    if x >= y:
        print(x, y)
    else:
        print(y, x)