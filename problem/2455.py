#지능형 기차
s = 0
l = []
for _ in range(4):
    a,b = map(int, input().split())
    s -= a
    s += b
    l.append(s)
    
    
print(max(l))