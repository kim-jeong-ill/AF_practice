#점수 계산

n = int(input())
r = 0
result = 0
k = list(map(int, input().split()))

for i in range(n):
    if k[i] == 1:
        r += 1
        result += r
    else:
        r = 0
        
print(result)