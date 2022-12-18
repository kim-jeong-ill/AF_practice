#ACM 호텔

T = int(input())

for _ in range(T):
    H,W,N = map(int, input().split()) #H:호텔 층 W: 호텔 방 N: 몇번째 손님
    share = H // N # 몫
    rest = H % N # 나머지
    print(rest, end = '') # 층
    print(share)