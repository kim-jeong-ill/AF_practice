#가장 긴 증가하는 수열
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [1] * n

for i in range(n): # 0부터 6까지
    for j in range(i): # 0부터 i - 1까지 i개
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j]+1) 
            # 예를 들어 30이면 30보다 작은 숫자 중에서 dp값이 가장 큰거
            # 그리고 그 값에 +1 -> dp[j] + 1

print(max(dp))


'''
 a = {10, 20, 10, 30, 20, 50}
 dp = [1,1,1,1,1,1]
 
 dp = [1, 2, 1, 3(2였다가 3됨), ...]
'''