#알고리즘 수업 - 삽입 정렬 1
'''
#question
insertion_sort(A[1..N]) { # A[1..N]을 오름차순 정렬한다.
    for i <- 2 to N {
        loc = i - 1;
        newItem = A[i];

        # 이 지점에서 A[1..i-1]은 이미 정렬되어 있는 상태
        while (1 <= loc and newItem < A[loc]) {
            A[loc + 1] <- A[loc];
            loc--;
        }
        if (loc + 1 != i) then A[loc + 1] = newItem;
    }
'''

import sys

n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
# a = 4 5 1 3 2

cnt = 0

for i in range(1,n):
    loc = i
    tmp = a[i]
    
    while 0 < loc and a[loc-1] > tmp:
        a[loc] = a[loc-1]
        loc -= 1
        cnt += 1
        
    if cnt == k:
        print(tmp)
        exit()
        
    a[loc] = tmp
        
print(-1)



'''
def insertion_sort(a):
    n = len(a)
    for i in range(1, n): # 1부터 n-1까지 
        j = i
        tmp = a[i]
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp
        
'''