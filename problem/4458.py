#첫글자를 대문자로

n = int(input())

for _ in range(n):
    l = list(map(str, input().split()))
    
    ans = []
    i = l[0]
    i = i[0].upper() + i[1:]
    
    
    print(i, end=' ' )
    for i in range(len(l)-1):
        print(l[i+1], end=' ')
    
    print()
        