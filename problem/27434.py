# 팩토리얼 3

n = int(input())
r = 1
while n > 1:
    r *= n
    n -= 1
    
print(r)