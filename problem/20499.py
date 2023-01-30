#Darius님 한타 안 함?

n = input().split('/')
k = int(n[0])
d = int(n[1])
a = int(n[2])

if k+a < d or d == 0:
    print('hasu')
else:
    print('gosu')