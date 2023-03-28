#이진수

t = int(input())

for _ in range(t):
    n = int(input())
    
    l = []
    while n > 0:
        rest = n % 2
        n = n // 2
        l.append(rest)
        
    for i in range(len(l)):
        if l[i] == 1:
            print(i, end = ' ')