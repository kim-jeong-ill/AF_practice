#숫자 카드

n = int(input())
having = input().split() # [6 3 2 10 -10]
    
m = int(input())
find = input().split() # [10 9 -5 2 3 4 5 -10]

having = list(map(int, having))
find = list(map(int, find))
having.sort()

result = []
for i in find:
    key = i
    #pl pc pr 첫번째 중간 마지막
    pl = 0
    pr = len(having) - 1

    while 1:
        pc = (pl + pr) // 2
        if having[pc] == key:
            result.append(1)
            break
        elif having[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            result.append(0)
            break
        
for j in result:
    print(j, end = ' ')