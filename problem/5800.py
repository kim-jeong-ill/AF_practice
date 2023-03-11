#성적 통계
import sys
input = sys.stdin.readline

n = int(input())

#Max 78, Min 23, Largest gap 46
for i in range(n):
    l = list(map(int, input().split()))
    l = l[1:]
    l.sort()
    s = -1
    for j in range(len(l)-1): # 5
        if l[j+1] - l[j] > s:
            s = l[j+1] - l[j]
    print('Class', i+1)
    print('Max {0}, Min {1}, Largest gap {2}'.format(max(l), min(l),s))