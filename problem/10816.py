#숫자카드 2
import sys

n = int(sys.stdin.readline()) # 상근이가 가진 카드 개수

l1 = list(map(int, sys.stdin.readline().split()))
# 6 3 2 10 10 10 -10 -10 7 3
l1.sort() #이거 nlogn인지 궁금함

m = int(sys.stdin.readline()) # find하는 카드들

l2 = list(map(int, sys.stdin.readline().split()))
# 10 9 -5 2 3 4 5 -10

#우선 이진 탐색 복습
#pr pl pc / 처음 끝 중간

#까먹어서 조금 찾아봄 if elif else 부분
#여기서 log n 
def binary_search(arr, key): # 또 까먹을 뻔 이진탐색은 정렬된 배열에서만 가능
    n = len(arr)
    
    pr = 0
    pl = n - 1
    while pr <= pl:
        pc = (pr + pl)//2
        
        if arr[pc] == key:
            return 1
        elif arr[pc] > key:
            pl = pc - 1
        else:
            pc = pc + 1
            
    return -1

#아니 븅진인가 이진탐색 구현해놓고 반복문 두개 쓰고 있네
ans = []
for i in l2:
    binary_search(l1, i)
    
    
for i in ans:
    print(i, end = ' ')