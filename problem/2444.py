#별 찍기 - 7

n = int(input())

i = 1
j1 = n

j1 -= 1
while i <= n:
    print(' ' * j1, end = '')
    print('*' * ((2*i)-1), end = '')
    print()
    i += 1
    j1 -= 1
    
i2 = 1
j2 = n-1
while i2 < n:
    print(' ' * i2, end = '')
    print('*' * ((2*j2)-1), end = '')
    print()
    i2 += 1
    j2 -= 1