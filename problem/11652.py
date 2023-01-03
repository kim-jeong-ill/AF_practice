#카드

import sys
input = sys.stdin.readline

n = int(input())
l1 = []
for _ in range(n):
    num = int(input())
    l1.append(num)
    
l2 = list(set(l1))

l3 = []
for i in l2:
    count = 0
    for j in l1:
        if i == j:
            count += 1
    l3.append(count)
    
large = l3.index(max(l3))

print(l2[large])