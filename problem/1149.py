#RGB 거리

n = int(input())
dp = [0] * n

for i in range(n):
    dp[i] = list(map(int, input().split()))
    
for j in range(1, n):
    # Red
    dp[j][0] += min(dp[j-1][1], dp[j-1][2])
    # Green
    dp[j][1] += min(dp[j-1][0], dp[j-1][2])
    # Blue
    dp[j][2] += min(dp[j-1][0], dp[j-1][1])
    
print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))