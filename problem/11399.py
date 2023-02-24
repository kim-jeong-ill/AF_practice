#ATM
import sys

n = int(sys.stdin.readline())

l = list(map(int, sys.stdin.readline().split()))

l.sort()

s = 0
s1 = 0
for i in l:
    s += i
    s1 += s

print(s1)