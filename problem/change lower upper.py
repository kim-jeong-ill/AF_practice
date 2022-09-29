s = input()
s = list(s)

tmp = []

for i in s:
    if i.isupper() == 1:
        tmp.append(i.lower())
    else:
        tmp.append(i.upper())
        
for j in tmp:
    print(j, end= '')