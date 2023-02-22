#정열적인 정렬
'''#왜 넌 안되는데;
#내장함수 쓰래
import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))


def qsort(a,left,right):
    pl = left
    pr = right
    x = a[(left+right)//2]
    
    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
            
    if left < pr: qsort(a, left, pr)
    if pl < right: qsort(a, pl, right)
        
def quick_sort(a):
    qsort(a,0,len(a)-1)

quick_sort(l)

for i in l:
    print(i, end=' ')
'''

import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

l.sort()

for i in l:
    print(i, end=' ')