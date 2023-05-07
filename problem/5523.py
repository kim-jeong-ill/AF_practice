#경기 결과

n = int(input())
cnt1 = 0
cnt2 = 0

for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        cnt1 += 1
    elif a == b:
        continue
    else:
        cnt2 += 1
        
print(cnt1, cnt2)