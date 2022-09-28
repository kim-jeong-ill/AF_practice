cnt = []

for _ in range(28):
    number = int(input())
    cnt.append(number)

new_cnt = []

i = 1
while i <= 30:
    if i in cnt:
        cnt.remove(i)
    else:
        new_cnt.append(i)
    i += 1
        
for j in new_cnt:
    print(j)
    