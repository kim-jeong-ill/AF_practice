#ACM 호텔

T = int(input())

for _ in range(T):
    h,w,n = map(int, input().split()) #h:호텔 층 w: 호텔 방 n: 몇번째 손님
    floor = n%h
    num = n//h+1
    if n % h == 0:
        floor = h
        num -= 1
    print(floor*100+num)