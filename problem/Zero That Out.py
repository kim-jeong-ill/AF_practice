#제로

n = int(input())

price = []

for _ in range(n):
    a = int(input())
    price.append(a)
    
for i in price:
    if price[i+1] == 0:
        price[i-1] = 0
    
print(price)