#최댓값
import sys

li = []

for _ in range(9):
    tmp = list(map(int, sys.stdin.readline().split()))
    li += tmp
    
print(max(li))
i = li.index(max(li))
ix = i // 9 + 1
iy = i % 9 + 1
print(ix, iy)