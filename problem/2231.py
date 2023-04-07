#분해합

    
n = int(input())  # 분해합을 입력값으로 받음

for i in range(1, n+1): 
    num = sum((map(int, str(i))))
    s = i + num
    if s == n:
        print(i)
        break
    if i == n:
        print(0)