#조합 0의 개수

'''
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
'''

# 비슷한 <문제1676>
import sys
input = sys.stdin.readline

n, r = map(int, input().split())

def count2(n):
    if n < 2:
        return 0
    count = 0
    while n >= 2:
        count += n // 2
        n = n // 2
    return count

def count5(n):
    if n < 5:
        return 0
    count = 0 
    while n >= 5:
        count += n // 5
        n = n // 5
    return count

two = count2(n) - count2(r) - count2(n-r)

five = count5(n) - count5(r) - count5(n-r)

print(min(two, five))