#Reverse

n = int(input())

for _ in range(n):
    a,b,c = input().split()
    b = int(b) - 1
    c = int(c) - 1
    a = list(a)
    for i in range(b, c+1):
        a.remove(i)
    for j in a:
        print(j, end = '')
    print()