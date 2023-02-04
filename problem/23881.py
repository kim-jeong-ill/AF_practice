#알고리즘 수업 - 선택 정렬 1
'''
def selection_sort(arr):
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
'''

'''
n, k = map(int, input().split()) # n=5, k=2

a = input().split()
a = list(map(int, a)) # a = [ 3 1 2 5 4 ]

count = 0
for i in range(len(a), 0, -1): #5,4,3,2,1까지
    last = i # 5
    for j in range(len(a)-1, 0, -1):
        if a[j] > a[last]:
            last = j 
            count += 1
    a[i], a[last] = a[last], a[i]
'''

import sys

n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

cnt = 0
ans = -1

def selection(arr):
    global cnt, ans
    
    for i in range(n-1, 0, -1): # i = 4321로 줄어듬
        last, idx = arr[0], 0 # 우선 첫번째 값으로 초기화, 예제1 : 3, 0
        for j in range(1, i+1): # 하나씩 정렬 last값이 정렬 되니까 그 전 꺼까지 j(즉 i+1까지)로 조절 예제1: list 2, 5까지
            if arr[j] > last: #이러면 계속 교환하는거 아닌가??
                last, idx = arr[j], j
                
        if arr[i] != arr[idx]:
            arr[i], arr[idx] = arr[idx], arr[i]
            cnt += 1
            
        if cnt == k:
            ans = f'{arr[idx]} {arr[i]}'
            
    return ans

print(selection(a))