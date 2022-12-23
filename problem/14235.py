# 크리스마스 선물
import heapq

n = int(input())
l = []

for _ in range(n):
    i = list(map(int, input().split()))
    if i[0] == 0:
        if len(l) == 0:
            print(-1)
        else:
            tmp = -heapq.heappop(l)
            print(tmp)
    else:
        for j in range(i[0]):
            heapq.heappush(l, -i[j+1])    