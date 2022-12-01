#별 찍기 - 6

n = int(input())

i = 0
j = n
while i < n:
    print(' ' * i, end = '')
    print('*' * ((j*2) - 1), end = '')
    print()
    i += 1
    j -= 1