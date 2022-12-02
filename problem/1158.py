#요세푸스 문제

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