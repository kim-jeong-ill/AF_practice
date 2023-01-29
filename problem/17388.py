#와글와글 숭고한

a,b,c = map(int, input().split())
l = [a,b,c]

if a+b+c >= 100:
    print('OK')
else:
    if a == min(l):
        print('Soongsil')
    elif b == min(l):
        print('Korea')
    else:
        print('Hanyang')