#제로

n = int(input())

price = []

for _ in range(n):
    a = int(input())
    if a == 0:
        price.pop()
    else:
        price.append(a)
    
sum = 0
for i in price:
    sum += i
    
print(sum)