#팀 나누기

a,b,c,d = map(int, input().split())

team1 = a + d
team2 = b + c

team1 = team1 // 2
team2 = team2 // 2

if team1 >= team2:
    print(team1 - team2)
else:
    print(team2 - team1)
    