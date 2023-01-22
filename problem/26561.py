#Population
#7초에 한명 die
#4초에 한명 born

n = int(input())

for _ in range(n):
    begining, period = map(int, input().split())
    die = period // 7
    born = period // 4
    print(begining - die + born)