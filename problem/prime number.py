'''
# 첫 번째 코드 : 시간 초과
limit_num = 1000000
check_num = int(limit_num ** 0.5)
prime_num = [True] * limit_num
p_n = []

for i in range(2, check_num+1):
    if prime_num[i] == True:
        for j in range(2*i, limit_num, i):
            prime_num[j] = False
        
for k in range(2, limit_num):
    if prime_num[k] == True:
        p_n.append(k)


m, n = map(int, input().split())

for a in range(m, n+1):
    if a in p_n:
        print(a)
'''

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    
    
m, n = map(int, input().split())

for i in range(m, n+1):
    if isPrime(i):
        print(i)