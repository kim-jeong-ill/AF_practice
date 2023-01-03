#진법 변환
import sys
input = sys.stdin.readline

n, b = map(int, input().split())

a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

answer = ''

while n != 0:
    answer += str(a[n%b]) #a[n%b] 허허
    n //= b
    
print(answer[::-1]) # reverse 까먹지 않기