# 앵그리 창영

n, w, h = map(int, input().split())

r = (w*w + h*h) ** 0.5

for _ in range(n):
    a = int(input())
    if a <= r:
        print('DA')
    else:
        print('NE')