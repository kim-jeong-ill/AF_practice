#피보나치 수열2

import sys
input = sys.stdin.readline

'''
# recursion - runtime error
# dp - index error
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
def fibo_dp(n):
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

x = int(input())

print(fibo_dp(x))
'''

'''
n = int(input())

d = [0] * (10001)
d[0] = 0
d[1] = 1
for i in range(2, 10001):
    d[i] = d[i-2] + d[i-1]

print(d[i])
'''

#??? 내 코드는 왜 안됨?
import sys
input = sys.stdin.readline

n = int(input())
fibo = [0,1]

for i in range(2, n+1):
    fibo.append(fibo[i-1] + fibo[i-2])
    
print(fibo[n])