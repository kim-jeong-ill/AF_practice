#올림픽

n, k  = map(int, input().split())

l = []
i = 0
for _ in range(n):
    if i == k:
        k = score[:]
    score = list(map(int, input().split()))
    l.append(score)
    i += 1
    
l.sort(key=lambda x : (x[0],x[1],x[2],x[3]))
l.reverse()

cnt = 0 
for j in l:
    cnt += 1
    if j == k:
        print(cnt)