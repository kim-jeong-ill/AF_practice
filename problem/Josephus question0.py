#요세푸스 문제0

n, k = map(int, input().split()) # 7 3

tmp = 0 
print('<', end = '')
for _ in range(n): # 3 6 9 12 -> 3 6 2 7
    tmp += k
    if n > tmp:
        print(tmp, end = ', ')
    else:
        temp = tmp % n
        print(temp)
        
        
print('>', end = '')