n = int(input())

for _ in range(n):
    num, s = input().split()
    for j in s:
        print(j*int(num), end = '')
    print()