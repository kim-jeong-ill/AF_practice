#알고리즘 수업 - 버블 정렬 1
#pypy3

import sys

a, k = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

cnt = 0

for i in range(a-1,0,-1): # 4~0까지 인덱스
    for j in range(i): # 
        if li[j] > li[j+1]: # 0~5까지
            li[j], li[j+1] = li[j+1], li[j]
            cnt += 1
            
            if cnt == k:
                if li[j] > li[j+1]:
                    li[j], li[j+1] = li[j+1], li[j]
                print(f'{li[j]} {li[j+1]}')
                exit()
                
print(-1)