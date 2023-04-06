#탁구 경기

n = int(input())

a = 0
b = 0
for _ in range(n):
    s = input()
    if s == 'D':
        a += 1
    elif s == 'P':
        b += 1
        
    if a == b-2 or b == a-2:
        ans1 = a
        ans2 = b
    

print('{}:{}'.format(ans1,ans2))