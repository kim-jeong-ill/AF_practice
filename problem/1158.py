#요세푸스 문제

"""
n, k = map(int, input().split())

l = [1] * n # [1,1,1,1,1,1,1] index 0123456  1회 [1,1,0,1,1,1,1]
a = []

k -= 1
for _ in range(n): # 7번만
    while 1:
        if l[k] == 0:
            k += k
            if k > n:
                k -= n
        else:
            break
    l[k] = 0
    a.append(k+1)
    k += k
    if k > n:
        k -= n
    
print('<', end = '')
for i in range(len(a)-1):
    print(a[i], end =', ')
print(a[-1], end = '>')
"""

"""
n, k = map(int, input().split())

l = [1] * n
ln = []

i = 0
while i < n:
    while 1:
        if l[k-1] == 0:
            k += 1
            if k > n:
                k -= n
        else:
            l[k-1] = 0
            ln.append(k)
            break
        k += k
        if k > n:
            k -= n
        i += 1
            
print('<', end = '')
for i in range(len(ln)-1):
    print(ln[i], end =', ')
print(ln[-1], end = '>')
"""

n, k = map(int, input().split())

l = [] # 1 2 3 4 5 6 7
for i in range(n):
    l.append(i+1)
    
ln = []
num = k-1

for _ in range(n):
    if len(l) > num:
        ln.append(l.pop(num))
        num += k-1
    elif len(l) <= num:
        num = num % len(l)
        ln.append(l.pop(num))
        num += k-1
        
print('<', end = '')
for i in range(len(ln)-1):
    print(ln[i], end =', ')
print(ln[-1], end = '>')