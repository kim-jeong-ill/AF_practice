#단어순서 뒤집기

N = int(input())

for i in range(N):
    s = input().split()
    s.reverse()
    print('Case #{0}:'.format(i+1), end = ' ')
    for i in s:
        print(i, end = ' ')