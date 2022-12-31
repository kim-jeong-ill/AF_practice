#가장 큰 증가 부분 수열

import sys
input = sys.stdin.readline

n = int(input())

l = list(map(int, input().split())) # [1 100 2 50 60 3 5 6 7 8]

dp = [1] * n
dp[0] = l[0]

for i in range(n):
    for j in range(i):
        if l[i] > l[j]:
            dp[i] = max(dp[i], dp[j]+l[i])
        else:
            dp[i] = max(dp[i], l[i])
            
print(max(dp))