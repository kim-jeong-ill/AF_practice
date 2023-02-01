#치킨 두 마리(...)

a, b = map(int ,input().split())

n = int(input())

if a+b >= 2*n:
    print(a+b-(2*n))
else:
    print(a+b)