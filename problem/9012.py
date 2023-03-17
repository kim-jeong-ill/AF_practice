#괄호
#

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
        cnt = 0
        for j in range(len(x)):
            if x[j] == ')':
                cnt -= 1
            if x[j] == '(':
                cnt += 1
            if cnt < 0:
                break
            
        if cnt >= 0:
            print('YES')
        else:
            print('NO')
        
    else:
        print('NO')
