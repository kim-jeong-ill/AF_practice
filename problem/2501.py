#약수 구하기

n, k = map(int, input().split())

l = []
for i in range(n):
    if n % (i+1) == 0:
        l.append(i+1)
        
if len(l) < k:
    print(0)
else:
    print(l[k-1])