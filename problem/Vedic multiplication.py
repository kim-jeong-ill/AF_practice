#푸앙이와 종윤이(베다수학 곱셈)

x, y = map(int, input().split())

a = 100 - x
b = 100 - y

c = 100 - (a+b)
d = a*b
q = d // 100
r = d % 100

print(a,b,c,d,q,r)
print(c+q, r)