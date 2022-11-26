#팀 나누기

a,b,c,d = map(int, input().split())

team1 = a + d
team2 = b + c

if team1 >= team2:
    print(team1 - team2)
else:
    print(team2 - team1)