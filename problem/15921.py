#수찬은 마린보이야!!

n = int(input())
if n == 0:
    print('divide by zero')
else:
    l = list(map(int, input().split()))

    average = sum(l)/n

    expected = 0

    for i in range(n):
        expected += l[i]/n

    if n == 0 or sum(l) == 0:
        print('divide by zero')
    else:
        print('{:.2f}'.format(average/expected))