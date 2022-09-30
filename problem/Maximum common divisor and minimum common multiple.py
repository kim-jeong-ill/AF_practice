#최대 공약수, 최소공배수
#최대공약수 - 유클리드 호제법
'''
a, b = map(int, input().split())

if b > a:
    tmp = a
    a = b
    b = tmp
#무조건 a가 크게 만듬

while 1:
    rest = a % b
    share = a // b
    if rest == 0:
        break
    a = share
    b = rest
    
            
print(share)
'''

a, b = map(int, input().split())

original_a = a
original_b = b

if b > a:
    tmp = a
    a = b
    b = tmp
    
while 1:
    rest = a % b
    if rest == 0:
        break
    a = b
    b = rest # 최대 공약수
    
print(b)
print(original_a*original_b//b)
