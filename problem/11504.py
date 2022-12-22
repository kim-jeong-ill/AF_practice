#돌려 돌려 돌림판

T = int(input())

for _ in range(T):
    n, length = map(int, input().split()) # 8 3
    
    x = input().split()
    x1 = int(''.join([i for i in x])) # 200
    
    y = input().split()
    y1 = int(''.join([i for i in y])) # 311
    
    dol = input().split() # 3 7 8 3 1 9 2 7
    dol2 = dol + dol[:length-1] # 3 7 8 3 1 9 2 7 3 7
    result = 0
    count = 0
    for i in range(n):
        result = int(''.join(dol2[i:i+length]))
        if x1 <= result <= y1:
            count += 1
    print(count)