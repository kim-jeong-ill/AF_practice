#이진수 변환

n = int(input())

l = []

while 1:
    r = n % 2 # 1, 0, 1, 0, 1, 1
    l.append(r)
    n = n // 2 # 53 -> 26 -> 13 -> 6 -> 3 -> 1
    if n <= 1:
        l.append(n)
        break
        
l.reverse()
for i in l:
    print(i, end='')