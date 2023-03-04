#점수 집계

T = int(input())

l = []
for _ in range(T):
    score = list(map(int,input().split()))
    score.sort()
    if (score[3] - score[1]) >= 4:
        print('KIN')
    else:
        s = 0
        for i in range(3):
            s += score[i+1]
        print(s)