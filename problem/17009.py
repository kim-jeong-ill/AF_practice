#Winning Score

cnt1 = 0
cnt2 = 0

for i in range(3,0,-1):
    n = int(input())
    cnt1 += n * i
    
for j in range(3,0,-1):
    n = int(input())
    cnt2 += n * j

if cnt1 > cnt2:
    print('A')
elif cnt1 < cnt2:
    print('B')
else:
    print('T')