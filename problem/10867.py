#중복 빼고 정렬하기
import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

l = list(set(l))

l.sort()

for i in l:
    print(i, end=' ')