#헛간 청약

n, w, h, l = map(int, input().split()) # 7 6

size1 = w // l
size2 = h // l

possible = size1 * size2

if possible >= n:
    print(n)
else:
    print(possible)