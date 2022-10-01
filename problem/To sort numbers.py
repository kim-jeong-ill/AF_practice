#수 정렬하기 3
#선택, 삽입, 버블
'''
n = int(input())

cnt = []

for _ in range(n):
    i = int(input())
    cnt.append(i) # cnt = [5,2,3,1,4,2,3,5,1,7]


for i in range(len(cnt)):
    for j in range(len(cnt)- i - 1):
        if cnt[j] > cnt[j+1]:
            tmp = cnt[j]
            cnt[j] = cnt[j+1]
            cnt[j+1] = tmp

for i in cnt:
    print(i)
'''
    
#수 정렬하기 1
#bubble sort
n = int(input())

cnt = []

for _ in range(n):
    i = int(input())
    cnt.append(i) # cnt = [5,2,3,1,4,2,3,5,1,7]


for i in range(len(cnt)):
    for j in range(len(cnt)- i - 1):
        if cnt[j] > cnt[j+1]:
            tmp = cnt[j]
            cnt[j] = cnt[j+1]
            cnt[j+1] = tmp

for i in cnt:
    print(i)