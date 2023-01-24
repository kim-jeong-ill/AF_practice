#소수

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    
a = int(input())
b = int(input())
l = []

for i in range(a, b+1):
    if isPrime(i) == True:
        l.append(i)
    
s = 0
for j in l:
    s += j
    
if len(l) == 0:
    print(-1)
else:
    print(s)
    print(min(l))