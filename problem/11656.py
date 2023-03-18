#접미사 배열

s = str(input())
l = []
for i in range(0, len(list(s))):
    l.append(s[i:])
    
l.sort()

for j in l:
    print(j)