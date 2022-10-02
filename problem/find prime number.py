#소수 구하기

n = 1000
prime_n = []


for i in range(2, n+1): # 2~ 1000
    for j in range(2,i): # 2부터 i-1인 수 까지가 j
        if i%j == 0: # 소수가 아니면 여기에서 막히고
            break
    else:
        prime_n.append(i) # 소수면 여기에 추가

N = int(input())

test_num = list(map(int, input().split()))

count = 0

for i in test_num:
    if i in prime_n:
        count += 1

print(count)