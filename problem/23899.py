#알고리즘 수업 - 선택 정렬 5
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

for i in range(n-1,0,-1): # 4 3 2 1
    if a == b:
        break
    idx = a.index(max(a[:i + 1]))
    if idx != i:
        a[idx], a[i] = a[i], a[idx]
        
if a == b:
    print(1)
else:
    print(0)