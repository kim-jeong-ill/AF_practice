#팩토리얼 2

n = int(input())

s = 1
for i in range(n):
    s *= i+1
    
print(s)