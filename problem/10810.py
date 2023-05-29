#공 넣기

n, m = map(int, input().split())
b = [0] * n

for _ in range(m):
    i, j, k = map(int, input().split())
    for x in range(i, j+1):
        b[x-1] = k
        
for i in range(n):
    print(b[i], end = ' ')