#점수 계산
l = []

for _ in range(8):
    n = int(input())
    l.append(n)

l1 = l[:]

l.sort()
l.reverse()

ans = []
for i in range(5):
    ans.append(l[i])
    
print(sum(ans))
    
x = []
for j in ans:
    if j in l1:
        x.append(l1.index(j) + 1)
        
x.sort()
for k in x:
    print(k, end = ' ')