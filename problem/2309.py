#일곱 난쟁이

l = []

for _ in range(9):
    a = int(input())
    l.append(a)
    
s = 0
for i in l:
    s += i
    
for i in range(8):
    for j in range(i+1, 9):
        if s - (l[i] + l[j]) == 100:
            first = l[i]
            second = l[j]
            
l.remove(first)
l.remove(second)

l.sort()
for i in l:
    print(i)