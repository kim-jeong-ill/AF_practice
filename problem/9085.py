# 더하기

t = int(input())

for _ in range(t):
    n = int(input())

    li = list(map(int, input().split()))

    s = 0
    for i in li:
        s += i

    print(s)