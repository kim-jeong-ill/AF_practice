#10부제

n = str(input())

l = input().split()

count = 0
for i in l:
    if i == n:
        count += 1
        
print(count)