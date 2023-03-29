#TGN

n = int(input())

for _ in range(n):
    l = list(map(int,input().split()))
    
    if l[0] + l[2] == l[1]:
        print('does not matter')
        
    elif l[0] + l[2] > l[1]:
        print('do not advertise')
    
    else:
        print('advertise')