#단어 뒤집기

T = int(input())

for _ in range(T):
    s = input().split()
    for i in s:
        word = i
        r_word = word[::-1]
        print(r_word, end =' ')