# 배수 찾기

n = int(input())

while 1:
    a = int(input())

    if a == 0:
        break

    if a % n == 0:
        if a < n:
            print('{} is NOT a multiple of {}.'.format(a, n))
        else:
            print('{} is a multiple of {}.'.format(a, n))
    else:
        print('{} is NOT a multiple of {}.'.format(a, n))