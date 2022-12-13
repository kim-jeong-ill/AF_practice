#별 찍기 - 15

n = int(input())

i = 1
j = n-1

if n == 1:
    print('*')
else:
    print(' '*(n-2), '*')
    while i < n:
        print(' '*(j-1), end = '')
        print('*', end = '')
        print(' '*(2*i-1), end='')
        print('*')
        i += 1
        j -= 1