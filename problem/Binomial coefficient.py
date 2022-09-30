#이항 계수

m, n = map(int, input().split())

i = m - n
a=1
b=1
c=1

while m > 0:
    a *= m
    m -= 1
while n > 0:
    b *= n
    n -= 1
while i > 0:
    c *= i
    i -= 1
    
print(a//(b*c))