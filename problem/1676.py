#팩토리얼 0의 개수

n = int(input())

factorial = 1

while n >= 1:
    factorial *= n
    n -= 1
    
factorial = list(str(factorial))

factorial.reverse()

i = 0
count = 0
while 1:
    if factorial[i] == '0':
        count += 1
        i += 1
    else:
        break
        
print(count)