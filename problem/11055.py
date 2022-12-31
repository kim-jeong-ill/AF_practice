#가장 큰 증가 부분 수열

n = int(input())

l = list(map(int, input().split())) # [1 100 2 50 60 3 5 6 7 8]

dp = [1] * n

