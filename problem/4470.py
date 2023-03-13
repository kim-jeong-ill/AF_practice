#줄번호

n = int(input())

l = []
for _ in range(n):
    s = input()
    l.append(s)
    
for i in range(n):
    print('{0}. '.format(i+1), end='')
    print(l[i])