#별 찍기 - 23

n = int(input())

if n == 2:
    print('** **')
    print(' *** ')
    print('** **')
else:
    print('*'*n, end='')
    print(' '*(2*(n-1)-1), end='')
    print('*'*n, end='')
    print()
    i = 1
    while i< n-1:
        print(' '*i, end='*')
        print(' '*(n-2), end='*')
        print(' '*(2*(n-i-1)-1), end='*')
        print(' '*(n-2), end='*')
        print()
        i += 1
    print(' '*(n-1), end='*')
    print(' '*(n-2), end='*')
    print(' '*(n-2), end ='*')
    print()
    j = 1
    while j < n-1:
        print(' '*(n-j-1), end='*')
        print(' '*(n-2), end='*')
        print(' '*(2*j-1),end='*')
        print(' '*(n-2), end='*')
        print()
        j += 1
    print('*'*n, end='')
    print(' '*(2*(n-1)-1), end='')
    print('*'*n, end='')