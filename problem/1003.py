#피보나치 함수, 누구미 마렵다
#https://datazzang.tistory.com/18
#위에 풀이 멋있네
'''
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
'''

T = int(input())


cnt0 = [1,0,1]
cnt1 = [0,1,1]

def fibo(num):
    length = len(cnt0)
    if num >= length:
        for i in range(length, num+1):
            cnt0.append(cnt0[i-2] + cnt0[i-1])
            cnt1.append(cnt1[i-2] + cnt1[i-1])
    print('{} {}'.format(cnt0[num], cnt1[num]))

for _ in range(T):
    x = int(input())
    fibo(x)
    