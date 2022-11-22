#피보나치 함수

T = int(input())

for _ in range(T):
    a = int(input())
    dp = [0] * (a+1)
    dp[0] = 1
    dp[1] = 1
    count = 0
    for i in range(2, a+1):
        dp[i] = dp[i-1] + dp[i-2]