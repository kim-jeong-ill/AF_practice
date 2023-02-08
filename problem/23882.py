#알고리즘 수업 - 선택 정렬 2
#아니 왜 안됨? -> import sys 해주자;
#pypy3로 함;

import sys

n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

cnt = 0

for i in range(n-1,0,-1):
    last, idx = a[0], 0
    for j in range(1, i+1):
        if a[j] > last:
            last, idx = a[j], j
        
    if a[i] != a[idx]:
        a[i], a[idx] = a[idx], a[i]
        cnt += 1
        
    if cnt == k:
        print(*a)
        exit()
        
print(-1)