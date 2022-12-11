#쉽게 푸는 문제

a, b = map(int, input().split())
l = []
sum = 0

for i in range(1, b+1):
    for j in range(i):
        l.append(i)
        
for k in range(a-1, b):
    sum += l[k]

print(sum)