#최소공배수

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
    b = rest # b는 최대공약수

print(original_a*original_b//b)