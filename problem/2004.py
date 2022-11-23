#조합 0의 개수

n, m = map(int, input().split())

def f(n): # f = factorial
    if n == 0:
        return 1
    else:
        sum = 1
        for i in range(1, n+1):
            sum *= i
        return sum

c = f(n) // (f(n-m) * f(m)) # c = combination
new_c = 
        


count = 0

for j in temp:
    if j == '0':
        count += 1
    else:
        break
        
print(count)
