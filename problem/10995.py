#별 찍기 - 20

n = int(input())

i = 1
if n == 1:
    print('*')
else:
    for _ in range(0, n):
        if i % 2 == 1:
            for _ in range(n-1):
                print('* ', end = '')
            print('*')
            i += 1
        else:
            for _ in range(n-1):
                print(' *', end = '')
            print(' *')
            i += 1