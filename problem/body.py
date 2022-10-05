#덩치

n = int(input())

body_list = []

for _ in range(n):
    x, y = map(int, input().split())
    body_list.append([x, y])
    
body_list.sort()
body_list.reverse()

