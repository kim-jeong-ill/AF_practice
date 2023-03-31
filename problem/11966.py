#2의 제곱인가?
n = int(input())

l = [2**i for i in range(31)]

if n in l:
    print(1)
else:
    print(0)