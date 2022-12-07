#0 = not cute /  1 = cute

n = int(input())
count1 = 0
count2 = 0

for _ in range(n):
    a = int(input())
    if a == 0:
        count1 += 1
    else:
        count2 += 1
        
if count1 > count2:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")