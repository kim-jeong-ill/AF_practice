#탁구 경기

n = int(input())

a = 0
b = 0
for _ in range(n):
    s = input()
    if s == 'D':
        a += 1
    else:
        b += 1
        

print('{}:{}'.format(a,b))