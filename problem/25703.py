#포인터 공부

n = int(input())

print('int a;')

if n>=2:
    print('int *ptr = &a;')
    
if n>=3:
    print('int **ptr2 = &ptr;')
    
if n>=4:
    for i in range(4,n+2):
        print('int', end=' ')
        print('*'*(i-1), end='')
        print('ptr', end='')
        print(i-1, '=', '&ptr', end='')
        print(i-2, end='')
        print(';')