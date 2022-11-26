#스택
import sys
input = sys.stdin.readline

n = int(input())
l = []

for _ in range(n):
    command = input().split()
    if len(command) > 1:
        command[1] = int(command[1])
    if command[0] == 'push':
        l.insert(0, command[1])
    elif command[0] == 'pop':
        if len(l) == 0:
            print(-1)
        else:
            print(l[0])
            l.remove(l[0])
    elif command[0] == 'size':
        print(len(l))
    elif command[0] == 'empty':
        if len(l) == 0:
            print(1)
        else:
            print(0)
    elif command[0] ==  'top':
        if len(l) == 0:
            print(-1)
        else:
            print(l[0])