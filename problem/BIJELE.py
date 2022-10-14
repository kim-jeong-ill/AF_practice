#킹, 퀸, 룩, 비숍, 나이트, 폰

# 1 1 2 2 2 8

bij = list(map(int, input().split())) #  0 1 2 2 2 7

ori = [1, 1, 2, 2, 2, 8]

cnt = []


i = 0
while i < len(bij):
    cnt.append(ori[i] - bij[i])
    i += 1
    
for j in cnt:
    print(j, end = ' ')