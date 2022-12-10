#피보나치 함수, 누구미 마렵다
import sys
input = sys.stdin.readline

def dp_fibo(n):
    l = [0] * 41
    l[1] = 1
    l[2] = 1
    for i in range(3, n+1):
        l[i] = l[i-1] + l[i-2]
    return l[n]


T = int(input())

for _ in range(T):
    a = int(input())
    b = list(str(a))
    count1 = 0
    count2 = 0
    for i in b:
        if i == '0':
            count1 += 1
        if i == '1':
            count2 += 1
    print(count1, count2)