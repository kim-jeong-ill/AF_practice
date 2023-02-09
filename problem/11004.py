#K번째 수
#알고리즘 책 참고 (당직때 한 4시간 본 듯;)
#아니 왜 퀵인데 안빨라
#https://anggeum.tistory.com/entry/%EB%B0%B1%EC%A4%80-11004%EC%A0%95%EB%A0%AC%ED%8C%8C%EC%9D%B4%EC%8D%AC-K%EB%B2%88%EC%A7%B8-%EC%88%98-%EA%B5%AC%ED%95%98%EA%B8%B0
import sys

n,k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

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
    

quick_sort(a)

print(a[k-1])