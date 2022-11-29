#홀수

l = []

for _ in range(7):
    n = int(input())
    l.append(n)
    
o = []
for i in l:
    if i % 2 == 1:
        o.append(i)
        
if len(o) == 0:
    print('-1')
else:
    sum = 0
    for k in o:
        sum += k
    print(sum)
    print(min(o))