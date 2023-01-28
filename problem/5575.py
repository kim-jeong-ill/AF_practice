#타임 카드

for _ in range(3):
    h,m,s,h1,m1,s1 = map(int,input().split())
    if s > s1:
        s1 += 60
        m1 -= 1
    ws = s1 - s
    if m > m1:
        m1 += 60
        h1 -= 1
    wm = m1 - m
    wh = h1 - h
    print(wh, wm, ws)