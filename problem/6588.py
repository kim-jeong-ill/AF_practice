#pypy3

'''
import sys

l = [1 for i in range(1000000)] # 1000000

#소수 판별
for i in range(2,1001):
    if l[i] == 1:
        for k in range(i+i, 1000000, i):
            l[k] = 0
            
while True:
    n = int(sys.stdin.readline())
    
    if n == 0:
        break
        
    for i in range(3, len(l)):
        if l[i]==1 and l[n-i]==1:
            print(n, '=', i, '+', n-i)
            break
'''

import sys

while True:
    answer =0
    num = int(sys.stdin.readline())
    if num == 0:
        break
    lit = [i for i in range(num,2,-1)]
    count = 0
    ans = []
    while lit:
        q = lit[0]
        ans.append(q)
        for i in lit:
            if i % q ==0:
                lit.remove(i)
                count += 1
    for i in range(len(ans)):
        for j in range(len(ans)):
            if (ans[i]+ans[j]) == num:
                answer = ans[i]
    if answer ==0:
        print("Goldbach's conjecture is wrong.")
    else:
        print(num,end=" = ");print(answer,end=" + ");print(num-answer)