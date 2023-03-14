#스택 수열
#message = True부분 참고함
#문제이해가 안됐었음
#https://assaeunji.github.io/python/2020-05-04-bj1874/
#설명 Good

n = int(input())

cnt = 0
stack = []
result = []
message = True

for _ in range(n):
    x = int(input())
    
    while cnt < x:
        cnt += 1
        stack.append(cnt)
        result.append('+')
    
    if stack[-1]==x:
        stack.pop()
        result.append('-')
        
    else:
        message = False
        break
        
if message == False:
    print('NO')
    
else:
    print('\n'.join(result))