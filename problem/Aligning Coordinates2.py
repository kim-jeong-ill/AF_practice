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