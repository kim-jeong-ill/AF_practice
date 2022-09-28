n = input().split(' ')
n = list(map(int, n))

result = n[1] - n[0]

if result < 0:
    result *= -1
print(result)