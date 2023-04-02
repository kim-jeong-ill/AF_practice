#남욱이의 닭장 

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    s = m*2 - n
    r = n - m
    print(s, r)