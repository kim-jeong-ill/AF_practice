#초콜릿 자르기
'''
n, m = map(int,input().split())

print(n*m-1)

'''


#25628
#햄버거 만들기

a,b = map(int,input().split())

a = a//2

if a <= b:
    print(a)
else:
    print(b)