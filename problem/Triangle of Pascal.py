#파스칼의 삼각형

n, k = map(int, input().split())

n -= 1
k -= 1

sum1 = 1
for _ in range(k):
    sum1 *= n
    n -= 1
    
sum2 = 1
for _ in range(k):
    sum2 *= k
    k -= 1
    
print(sum1 // sum2)