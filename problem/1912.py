#연속합
import sys
input = sys.stdin.readline

n = input()
l = input().split() # [1,2,3,4] 이런 식으로 저장 됨
l = list(map(int, l))

max1 = max(l)
l.remove(max1)
max2 = max(l)

print(max1 + max2)