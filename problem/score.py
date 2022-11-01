#시험 점수

x = 0
y = 0

a,b,c,d = map(int, input().split())
e,f,g,h = map(int, input().split())

x = a + b + c + d
y = e + f + g + h

if x >= y:
    print(x)
else:
    print(y)