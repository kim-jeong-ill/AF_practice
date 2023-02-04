#나이 계산하기

y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())
man = 0
if m1 < m2:
    man = y2-y1
elif m1 == m2:
    if d1 <= d2:
        man = y2-y1
    else:
        man = y2-y1-1
else:
    man = y2-y1-1
count_old = y2-y1+1
year_old = y2-y1
print(man)
print(count_old)
print(year_old)