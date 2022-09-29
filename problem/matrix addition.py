'''
# EOFerror 런타임 에러
m_n = input().split(' ')

m_n = list(map(int, m_n)) # m_n[0] == n , m_n[1] == m

w = m_n[0]
h = m_n[1]

cnt_1 = []
cnt_2 = []

for _ in range(h): #세로
    width_1 = input().split(' ')
    width_1 = list(map(int, width_1))
    for a in width_1:
        cnt_1.append(a)
        
for _ in range(h):
    width_2 = input().split(' ')
    width_2 = list(map(int, width_2))
    for b in width_2:
        cnt_2.append(b)
    
result_cnt = []
i = 0
while i < len(cnt_1):
    result_cnt.append(cnt_1[i] + cnt_2[i])
    i += 1
    
j = 0
tmp = 1
while j < len(result_cnt):
    print(result_cnt[j], end = ' ')
    if tmp % w == 0:
        print()
    j += 1
    tmp += 1
'''

cnt_1 = []
cnt_2 = []

n, m = map(int, input().split(' ')) # 행 n, 열 m 가로:3,세로:3 들어옴

for width in range(n): # width를 3번 받음
    width = list(map(int, input().split(' '))) # 한 줄 받기
    cnt_1.append(width)
    
for width in range(n):
    width = list(map(int, input().split(' ')))
    cnt_2.append(width)
    

for width in range(n): # 가로
    for height in range(m): # 세로
        print(cnt_1[width][height] + cnt_2[width][height], end = ' ')
    print()
        