#숫자의 개수 (맞왜틀?)
'''
a = int(input())
b = int(input())
c = int(input())

result = a * b * c
print(result)
cnt = [0,0,0,0,0,0,0,0,0,0]


while result >= 1:
    a = result % 10
    if a == 0:
        cnt[0] += 1
    elif a == 1:
        cnt[1] += 1
    elif a == 2:
        cnt[2] += 1
    elif a == 3:
        cnt[3] += 1
    elif a == 4:
        cnt[4] += 1
    elif a == 5:
        cnt[5] += 1
    elif a == 6:
        cnt[6] += 1
    elif a == 7:
        cnt[7] += 1
    elif a == 8:
        cnt[8] += 1
    else:
        cnt[9] += 1
    result = result // 10
    
for i in cnt:
    print(i)
'''

a = int(input())
b = int(input())
c = int(input())

result = list(str(a * b * c))
for i in range(10):
    print(result.count(str(i)))
