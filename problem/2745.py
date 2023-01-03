#진법 변환 1

a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = list(a)

n, b = map(str, input().split())

b = int(b)

n = list(n)
n.reverse()

num = 0

j = 1
for i in n:
    num += int(a.index(i))*(j)
    j *= b
    
    
print(num)