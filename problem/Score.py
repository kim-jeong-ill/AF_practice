#ox 퀴즈


n = int(input())

for _ in range(n):
    s = str(input())
    o = s.split('X')
    score = 0
    
    for i in o:
        sum = 0
        j = 0
        for j in range(len(i)):
            sum += j
        score += sum
    print(score)

