#치킨댄스를 추는 곰곰이

n = int(input())
cnt = 0
for _ in range(n):
    k = input()
    if int(k[2:]) <= 90:
        cnt += 1
print(cnt)