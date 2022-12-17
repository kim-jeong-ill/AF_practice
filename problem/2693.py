#N번재로 큰 수

T = int(input())

for _ in range(T):
    l = input().split()
    l = list(map(int, l))
    l.sort()
    print(l[-3])