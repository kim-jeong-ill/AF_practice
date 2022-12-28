#뜨거운 붕어빵

n, m = map(int, input().split())

for _ in range(n):
    b = str(input())
    b = list(b)
    b.reverse()
    for i in b:
        print(i, end='')
    print()