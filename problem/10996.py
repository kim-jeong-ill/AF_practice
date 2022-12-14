#별 찍기 - 21

n = int(input())

if n == 1:
    print('*')
else:
    for i in range(n*2):
        if i % 2 == 0:
            for j in range(n):
                if j % 2 == 0:
                    print('*', end='')
                else:
                    print(' ', end='')
        else:
            for j in range(n):
                if j % 2 == 0:
                    print(' ', end='')
                else:
                    print('*', end='')
        print()