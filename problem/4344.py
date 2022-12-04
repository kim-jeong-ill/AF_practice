#평균은 넘겠지

C = int(input())

for _ in range(C):
    score = input().split()
    score = list(map(int, score))
    people = score[0]
    score.remove(score[0])
    sum_score = 0
    for i in score:
        sum_score += i
    avg = sum_score / people
    count = 0
    for i in score:
        if i > avg:
            count += 1
    answer = "{:.3f}".format(count / people * 100)
    print(answer, end = '')
    print('%')