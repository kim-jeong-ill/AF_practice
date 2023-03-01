#생일

n = int(input())

l = []

for _ in range(n):
    a = list(map(str, input().split()))
    l.append(a)
    
l.sort(key=lambda a : (int(a[3]),int(a[2]),int(a[1])))

print(l[-1][0])
print(l[0][0])