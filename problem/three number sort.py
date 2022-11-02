#세 수 정렬

a, b, c = map(int, input().split())
    
l = []

l.append(a)
l.append(b)
l.append(c)

l.sort()

for i in l:
    print(i, end = ' ')