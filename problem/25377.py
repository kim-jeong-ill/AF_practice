# 빵

n = int(input())
max1 = -1
for _ in range(n):
    a,b = map(int,input().split())
    if a <= b:
        max1 = b
        
print(max1)