#덱2

import sys
input = sys.stdin.readline

n = int(input())

l = []

for _ in range(n):
    a = input().split()
    a = list(map(int, a))
    
    if a[0] == 1:
        l.insert(0, a[1])
    elif a[0] == 2:
        l.insert(-1, a[1])
    elif a[0] == 3:
        if len(l) != 0:
            print(l[0])
            l.remove(l[0])
        else:
            print(-1)
            
    elif a[0] == 4:
        if len(l) != 0:
            print(l[-1])
            l.remove(l[-1])
        else:
            print(-1)
    elif a[0] == 5:
        print(len(l))
    elif a[0] == 6:
        if len(l) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 7:
        if len(l) != 0:
            print(l[0])
        else:
            print(-1)
    else:
        if len(l) != 0:
            print(l[-1])
        else:
            print(-1)