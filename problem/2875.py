#대회

n,m,k =map(int, input().split())

t = 0

while 1:
    n -= 2
    m -= 1
    if n < 0 or m < 0 or (n+m) < k:
        break
    t += 1
    
print(t)