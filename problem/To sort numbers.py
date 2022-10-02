#수 정렬하기 3
#선택, 삽입, 버블
import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n): # 크기 10001의 리스트에 숫자가 들어오면 그 숫자를 리스트인덱스에 맞게 더해줌!!
    num_list[int(sys.stdin.readline())] += 1
    
for i in range(10001):
    if num_list != 0: 
        for j in range(num_list[i]): # 리스트 인덱스에 숫자가 있는만큼 
            print(i)

    
#수 정렬하기 1
#bubble sort
'''
n = int(input())

cnt = []

for _ in range(n):
    i = int(input())
    cnt.append(i)


for i in range(len(cnt)):
    for j in range(len(cnt)- i - 1):
        if cnt[j] > cnt[j+1]:
            tmp = cnt[j]
            cnt[j] = cnt[j+1]
            cnt[j+1] = tmp

for i in cnt:
    print(i)
'''

#수 정렬하기 2
#input이 아닌 sys의 sys.stdin.readline을 사용해서
'''
import sys
n = int(input())

cnt = []

for _ in range(n):
    cnt.append(int(sys.stdin.readline()))
    
cnt.sort()

for i in cnt:
    print(i)
'''