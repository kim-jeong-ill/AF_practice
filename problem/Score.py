#ox 퀴즈

'''
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
'''

'''
N = int(input())

count = 0

while count < N:
    n = str(input())
    o = n.split('X')
    score = 0
    for i in o:
        sum = 0
        j = 0
        while j <= len(i):
            sum += j
            j += 1
        score += sum
    print(score)
    count += 1
'''

'''
#단어의 개수
n = str(input())

s = n.split(' ')

if s[0] == '':
    s.remove('')
if s[-1] == '':
    s.remove('')

count = 0
    
for i in s:
        count += 1
    
print(count)
'''

#단어 공부
n = str(input())

n.upper()

N = list(set(n))

