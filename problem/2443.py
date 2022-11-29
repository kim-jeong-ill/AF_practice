#별 찍기 - 6

n = int(input())

i = 0
while i <= n:
    j = n
    while j > 0:
        print(' ' * i, end = '')
        print('*' * ((j*2)-1), end = '')
        j -= 1
    print()
    i += 1