#펠린드롬수

while 1:
    n = input()
    n = list(map(int,n))
    
    if n[0] == 0:
        break
    
    if len(n) == 1:
        print("yes")
    elif len(n) == 2:
        if n[0] == n[-1]:
            print("yes")
        else:
            print("no")
    elif len(n) == 3:
        if n[0] == n[-1]:
            print("yes")
        else:
            print("no")
    else:
        if n[0] == n[-1] and n[1] == n[-2]:
            print("yes")
        else:
            print("no")