#커트라인
import sys
input = sys.stdin.readline

n, k = map(int,input().split())

l = list(map(int, input().split()))
l.sort()
l.reverse()

print(l[k-1])