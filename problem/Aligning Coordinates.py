#좌표 정렬하기
import sys
input = sys.stdin.readline

n = int(input())
coordinate = []

for _ in range(n):
    x, y = map(int, input().split())
    coordinate.append([x,y])
    
    
coordinate.sort()

for i in coordinate:
    print(i[0],i[1])