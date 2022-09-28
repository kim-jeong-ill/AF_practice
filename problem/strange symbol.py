def strange_symbol(a,b):
    return (a+b)*(a-b)

n = input().split(' ')
n = list(map(int, n))

print(strange_symbol(n[0],n[1]))