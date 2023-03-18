#에디터
import sys
input = sys.stdin.readline

s = list(str(input()))
m = int(input())

cnt = len(s)

for _ in range(m):
    command = list(map(str, input().split()))
    
    if command[0] == 'L':
        if cnt > 0:
            cnt -= 1
        
    elif command[0] == 'D':
        if cnt < len(s):
            cnt += 1
        
    elif command[0] == 'B':
        if cnt > 0:
            s.remove(s[cnt-1])
    
    else:
        s.insert(cnt, command[1])
        cnt += 1
        
for i in s:
    print(i, end='')