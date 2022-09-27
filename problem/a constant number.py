n = input().split(' ')
cnt = []

for i in n:
    cnt.append(i[::-1])
    
a = cnt[0]
b = cnt[1]

if a > b:
    print(a)
else:
    print(b)