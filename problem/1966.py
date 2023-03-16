#프린터 큐
#https://assaeunji.github.io/python/2020-05-04-bj1966/
'''
3 # 3번
1 0 # n, m
5 # 중요도 -> n이 1이니까 1개라서 중요도 하나만 나옴
4 2
1 2 3 4
6 0
1 1 9 1 1 1
'''

T = int(input())

for _ in range(T):
    n, m = map(int ,input().split())
    l = list(map(int, input().split()))
    idx = list(range(len(l)))
    
    idx[m] = 'target'
    
    order = 0
    
    while 1:
        if l[0] == max(l):
            order += 1
            
            if idx[0] == 'target':
                print(order)
                break
            else:
                l.pop(0)
                idx.pop(0)
        
        else:
            l.append(l.pop(0))
            idx.append(idx.pop(0))
        