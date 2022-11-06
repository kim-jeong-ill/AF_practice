#평균 점수

l = []

for _ in range(5):
    score = int(input())
    l.append(score)
    
i = 0


while i < 5:
    if l[i] <= 40:
        l[i] = 40
    i += 1
    
    
sum = 0
for j in l:
    sum += j

avg = sum // 5

print(avg)