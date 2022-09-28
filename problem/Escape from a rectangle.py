n = input().split(' ')
n = list(map(int, n))

x1 = n[0]
x2 = n[2]-n[0]
y1 = n[1]
y2 = n[3]-n[1]

cnt = []

cnt.append(x1)
cnt.append(x2)
cnt.append(y1)
cnt.append(y2)

cnt.sort()

print(cnt[0])