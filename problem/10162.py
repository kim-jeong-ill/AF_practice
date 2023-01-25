#전자레인지

n = int(input())

#a = 300, b = 60, c = 10
a = 300
b = 60
c = 10
share1 = 0
share2 = 0
share3 = 0

if n >= a:
    share1 = n // a
    rest1 = n % a
    n = rest1

if n >= b:
    share2 = n // b
    rest2 = n % b
    n = rest2
    
if n >= c:
    share3 = n // c
    rest3 = n % c
    
if rest3 == 0:
    print(share1, share2, share3)
else:
    print(-1)
    
'''
T = int(input())

if T % 10 != 0:
    print(-1)
else:
    A = B = C = 0
    A = T // 300
    B = (T % 300) // 60
    C = (T % 300) % 60 // 10
    print(A, B, C)
'''
print()