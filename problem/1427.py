#소트인사이트

n = list(str(input()))
n = list(map(int, n))

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
    

quick_sort(n)

n.reverse()

for i in n:
    print(i, end='')