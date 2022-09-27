#검증수

n = input().split(' ')

n = list(map(int,n))

sum = 0

for i in n:
    sum += i*i
    
print(sum%10)