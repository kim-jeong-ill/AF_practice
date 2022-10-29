#모음의 개수

while 1:
    n = input()
    n = n.lower()
    if n == '#':
        break
    n = list(n)
    count = 0
    for i in n:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            count += 1
    print(count)