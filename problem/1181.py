#단어 정렬
import sys

n = int(sys.stdin.readline())
l = []

for _ in range(n):
    l.append(sys.stdin.readline().strip())
l = set(l)
l = list(l)
l.sort()
l.sort(key = len)


for i in l:
    print(i)