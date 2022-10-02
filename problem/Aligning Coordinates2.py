import sys
input = sys.stdin.readline

n = int(input())
coordinate = []

for _ in range(n):
    x, y = map(int, input().split())
    coordinate.append([y,x])
    
    
coordinate.sort()

for i in coordinate:
    print(i[1],i[0])
    
'''
import sys
n = int(sys.stdin.readline())
so = []
for i in range(n):
    so.append(list(map(int, sys.stdin.readline().split())))
so.sort(key=lambda x: (x[1], x[0]))
for i in so:
    print(i[0], i[1])
'''