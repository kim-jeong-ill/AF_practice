#do not touch anything

a,b,c = map(int,input().split())

if a % c == 0:
    result1 = a//c
else:
    result1 = a // c + 1
    
if b % c == 0:
    result2 = b//c
else:
    result2 = b // c + 1

print(result1 * result2)