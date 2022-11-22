#1,2,3 더하기

T = int(input())

for _ in range(T):
    dp = [0] * 12
    n = int(input())
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])