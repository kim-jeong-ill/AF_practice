#영화감독 숌

n = int(input())

count = 1
k = 665
while 1:
    k += 1
    i = 0
    while i < len(str(k)):
        i = str(i)
        if k[i] == 6 and k[i+1] == 6 and k[i+2] == 6:
            count += 1
            break
        i = int(i)
    i += 1
    if count == n:
        break
        
print(k)