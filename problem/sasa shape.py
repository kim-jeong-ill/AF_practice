#SASA 모형을 만들어보자

n, m = map(int, input().split())

n = n // 2
m = m // 2

max_count = n

if max_count >= m:
    max_count = m
    
print(max_count)