import sys
n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n): # 크기 10001의 리스트 중에서 n개 만큼만 0이 아닌 1로 만들어줌
    num_list[int(sys.stdin.readline())] += 1

print(num_list)
    
for i in range(10001):
    if num_list != 0: # 1인 것들에만 
        for j in range(num_list[i]):
            print(i)