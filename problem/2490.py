#윷놀이

for _ in range(3):
    l = list(map(int ,input().split()))
    cnt = 0
    for i in l:
        if i == 1:
            cnt += 1
    if cnt == 0:
        print('D')
    elif cnt == 1:
        print('C')
    elif cnt == 2:
        print('B')
    elif cnt == 3:
        print('A')
    else:
        print('E')