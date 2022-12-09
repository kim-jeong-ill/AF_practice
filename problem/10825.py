#국영수 (국연수?)

n = int(input())
l = []

for _ in range(n):
    name, a, b, c = map(str, input().split())
    l.append((name, a, b, c))
    
l.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in l:
    print(i[0])