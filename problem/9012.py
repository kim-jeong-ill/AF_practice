#괄호
#개수로 하는거 안되네 ㅋㅋ;

T = int(input())

for _ in range(T):
    x = input()
    x = list(x)
    count1 = 0
    count2 = 0
    for i in x:
        if i == '(':
            count1 += 1
        else:
            count2 += 1
    if count1 == count2:
        print('YES')
    else:
        print('NO')
