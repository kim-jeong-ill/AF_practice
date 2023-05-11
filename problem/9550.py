#아이들은 사탕을 좋아해

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    cnt = 0
    for i in l:
        if i < k:
            continue
        else:
            cnt += i // k
    print(cnt)