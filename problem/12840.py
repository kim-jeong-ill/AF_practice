#창용이의 시계
'''
import sys

h, m, s = map(int, sys.stdin.readline().split())

for _ in range(int(sys.stdin.readline())):
    q =  list(map(int, sys.stdin.readline().split())) 
    if q[0] == 3:
        print(h, m, s)
    elif q[0] == 1:
        change = q[1]
        changes = change % 60
        change = change // 60
        changem = change % 60
        change = change // 60
        changeh = change
        h += changeh
        m += changem
        s += changes
        if s >= 60:
            m += 1
            s // 60
        if m >= 60:
            h += 1
            m // 60
        if h >= 24:
            h -= 24
    elif q[0] == 2:
        change = q[1]
        changes = change % 60
        change = change // 60
        changem = change % 60
        change = change // 60
        changeh = change
        h -= changeh
        m -= changem
        s -= changes
        if h < 0:
            h += 24
        if m < 0:
            m += 60
            h -= 1
        if s < 0:
            s += 60
            m -= 1
'''

import sys

h, m, s = map(int, sys.stdin.readline().split())
for _ in range(int(sys.stdin.readline())):
    li = list(map(int, sys.stdin.readline().split()))
    if len(li) == 1 and li[0] == 3:
        print(h, m, s)
    else:
        t = h*3600 + m*60 + s
        t += (li[1] if li[0] == 1 else -li[1]) # li[0] == 1이면 앞에꺼, 아니면 else 뒤에꺼
        if t < 0:
            t += 86400
        t = t%86400
        h, m, s = t//3600, (t%3600)//60, t%60