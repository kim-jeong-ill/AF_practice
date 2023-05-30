# 플러그
import sys
input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
    a = int(input())
    l.append(a)
    
s = 0
for i in l:
    s += i
    
print(s - (n-1))