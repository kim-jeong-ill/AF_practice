#덱
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

deque1 = deque()

for _ in range(n):
    command = input().split()
    if command[0] == "push_front":
        deque1.appendleft(command[1])
    elif command[0] == "push_back":
        deque1.append(command[1])
    elif command[0] == "pop_front":
        if len(deque1) == 0:
            print(-1)
        else:
            print(deque1.popleft())
    elif command[0] == "pop_back":
        if len(deque1) == 0:
            print(-1)
        else:
            print(deque1.pop())
    elif command[0] == "size":
        print(len(deque1))
    elif command[0] == "empty":
        if len(deque1) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if len(deque1) != 0:
            print(deque1[0])
        else:
            print(-1)
    elif command[0] == "back":
        if len(deque1) != 0:
            print(deque1[-1])
        else:
            print(-1)