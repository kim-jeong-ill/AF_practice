#파일 옮기기

a, b = map(int, input().split()) # 1 2 
c, d = map(int, input().split()) # 3 4

x = a + d
y = c + b

min_count = x

if min_count > y:
    min_count = y
    
print(min_count)