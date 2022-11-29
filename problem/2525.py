#오븐 시계

a, b = map(int, input().split())
c = int(input())

m = b + c

while m >= 60:
    if m >= 60:
        m -= 60
        a += 1
    
while a >= 24:
    if a >= 24:
        a -= 24
    
print(a, m)