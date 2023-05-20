# 영수증

n = int(input())

l = []

for _ in range(9):
    a = int(input())
    l.append(a)
    
result = n - sum(l)

print(result)