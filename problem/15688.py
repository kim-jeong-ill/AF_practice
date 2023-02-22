#수 정렬하기 5

import sys 

n = int(sys.stdin.readline())

l = []
for _ in range(n):
    a = int(sys.stdin.readline())
    l.append(a)
    
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
    print(i)