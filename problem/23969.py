#알고리즘 수업 - 버블 정렬 2
#pypy3

import sys

n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

cnt = 0

for i in range(n-1,0,-1):
    for j in range(i):
         if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                cnt += 1
                
                if cnt == k:
                    for x in a:
                        print(x, end=' ')
                    exit()
                    
print(-1)