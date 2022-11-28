#세 수
import sys
input = sys.stdin.readline

l = list(map(int, input().split()))

for i in range(1,3):
    if l[i] < l[i-1]:
        tmp = l[i]
        l[i] = l[i-1]
        l[i-1] = tmp

print(l[1])