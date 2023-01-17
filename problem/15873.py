#공백 없는 A+B

n = list(input())

a = int(''.join(n[0:-1]))

b = int(n[-1])

print(a+b)