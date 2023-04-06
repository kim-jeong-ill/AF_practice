#바구니 뒤집기

n, m = map(int,input().split())

l = []

for k in range(n):
    l.append(k+1)
    
for _ in range(m):
    i, j = map(int,input().split())
    
    l = l[:i-1] + l[i-1:j][::-1] + l[j:]
    
for i in l:
    print(i, end=' ')