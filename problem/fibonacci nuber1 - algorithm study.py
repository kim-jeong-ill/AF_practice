#알고리즘 수업 - 피보나치 수열 1

'''
def fib_recursion(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fib_recursion(n-1) + fib_recursion(n-2)

def fib_dp(n):
    dp_list = [0] * (n+1)
    dp_list[1] = 1
    dp_list[2] = 1
    dp_count = 0
    for i in range(3, n+1):
        dp_list[i] = dp_list[i-1] + dp_list[i-2]
        dp_count += 1
    return dp_count

x = int(input())

print(fib_dp(x), fib_dp(x))

'''

def fib(n):
    global count_fib
    count_fib += 1
    if n == 1 or n == 2:
        count_fib -= 1
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))

dp = {1 : 1, 2 : 1}
def fib_dp(n):
    global count_dp
    # n이 dp table에 있는 경우
    if n in dp:
        return dp[n]
    # n이 dp table에 없는 경우
    else:
        dp[n] = fib_dp(n - 1) + fib_dp(n  - 2)
        count_dp += 1
        return dp[n]
    
n = int(input())
count_fib, count_dp = 0, 0
fib(n)
fib_dp(n)
# count_fib에 1, 2
print(count_fib + 1, count_dp)