#주사위 세 개

a,b,c = map(int, input().split())

if a == b and a == c and b == c: #3개가 같을때
    print(10000 + a * 1000)
elif a == b and a != c: #2개가 같을 때
    print(1000 + a * 100)
elif a == c and a != b:
    print(1000 + a * 100)
elif b == c and c != a:
    print(100 + b * 100)
else:
    max = 0
    if max < a:
        max = a
    elif max < b:
        max = b
    elif max < c:
        max = c
    print(max * 100)