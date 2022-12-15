#수 찾기
import sys
input = sys.stdin.readline

a = input()
n = input().split()
b = input()
m = input().split()

n = list(map(int, n))
m = list(map(int, m))

n.sort()

result = []
for i in m:
    pl = 0
    pr = len(n) - 1
    key = i
    while 1:
        pc = (pl + pr) // 2
        if key == n[pc]:
            result.append(1)
            break
        elif n[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            result.append(0)
            break
            
for j in result:
    print(j)