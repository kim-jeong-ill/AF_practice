#2진수 뒤집기

n = int(input())

l = []
# 13 -> 1101
while n != 0:
    if n % 2 == 0:
        l.append(0)
    else:
        l.append(1)
    n //= 2
    
length = len(l) - 1 # 3
result = 0
for i in l:
    result += (2 ** length) * i
    length -= 1
    
print(result)