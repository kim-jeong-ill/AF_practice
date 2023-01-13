#나는 행복합니다~

n,m,k = map(int, input().split()) # n=세로 m=가로 k=관중석번호

print(k//m, k%m)


#Cupcake Party - 24568
a = int(input())
b = int(input())

result = (a*8 + b*3)

if result <= 28:
    print(0)
else:
    print(result - 28)