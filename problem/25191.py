#치킨댄스를 추는 곰곰이를 본 임스

n = int(input())
a,b = map(int, input().split())

if n >= (a//2 + b):
    print(a//2 + b)
else:
    print(n)