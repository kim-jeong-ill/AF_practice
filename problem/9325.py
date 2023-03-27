#얼마?

t = int(input())

for _ in range(t):
    s = int(input())
    n = int(input())
    tmp = 0
    for _ in range(n):
        a,b = map(int ,input().split())
        tmp += a*b
    print(s + tmp)