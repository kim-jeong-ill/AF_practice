#수 뒤집기

T = int(input())

for _ in range(T):
    num = int(input())
    a = num
    b = list(str(num))
    b.reverse()
    b = ''.join(b)
    b = int(b)
    result = a + b
    pc = len(str(result))//2 
    result = list(str(result))
    count = 0
    for i in range(pc):
        if result[i] == result[-(i+1)]:
            count += 1
    if count == pc:
        print('YES')
    else:
        print('NO')