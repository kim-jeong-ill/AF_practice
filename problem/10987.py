#모음의 개수

s = str(input())
s = list(s)

cnt = 0

for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        cnt += 1
        
print(cnt)