#Baseball

n = int(input())

for _ in range(n):
    l1 = []
    l2 = []
    for _ in range(9):
        a,b = map(int ,input().split())
        l1.append(a)
        l2.append(b)
        
    if sum(l1) == sum(l2):
        print('Draw')
    elif sum(l1) > sum(l2):
        print('Yonsei')
    else:
        print('Korea')