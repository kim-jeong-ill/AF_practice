#MBTI

n = input()
a = int(input())

cnt = 0
for _ in range(a):
    tmp = input()
    if n == tmp:
        cnt += 1
        
print(cnt)