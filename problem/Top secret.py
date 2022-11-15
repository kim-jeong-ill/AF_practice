#!밀비 급일

secret = " "

while 1:
    secret = input()
    if secret == 'END':
        break
    secret = list(secret)
    secret.reverse()
    for i in secret:
        print(i, end = '')
    print()