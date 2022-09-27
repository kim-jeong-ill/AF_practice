n = int(input())

score = input().split(' ')
score = list(map(int, score))
max_score = max(score)
cnt = []

for i in score:
    a = i/max_score*100
    cnt.append(a)

score_sum = 0
for j in cnt:
    score_sum += j
    
print(score_sum / n)