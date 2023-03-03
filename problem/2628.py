#종이자르기

n, m = map(int, input().split()) 

row = [0, n]
column = [0, m]

for _ in range(int(input())):
    r, line = map(int, input().split())
    if r == 1:
        row.append(line)
    else:
        column.append(line)
        
row.sort()
column.sort()

ans1 = []
ans2 = []

for i in range(len(row)-1):
    ans1.append(row[i+1]-row[i])
for j in range(len(column)-1):
    ans2.append(column[j+1]-column[j])
    
print(max(ans1)*max(ans2))