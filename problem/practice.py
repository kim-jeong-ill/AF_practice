'''
def counter():
    i = 0
    def count():
        nonlocal i
        i += 1
        return i
    return count
'''

'''
x = input()
x.split(' ')
sen = x[0]
num = int(x[1])

print(sen)
print(num)
'''
'''
score = map(int, input().split())

print(score)
'''

'''
n = int(input())
n = list(str(n))
n.reverse()
n = ''.join(n)
print(n)
'''


'''
n = int(input())
l = []

while 1:
    share = n // 2
    rest = n % 2
    l. append(rest)
    if share == 0:
        break
    n = share

print(l)
'''


q = input().split()
q = list(map(int, q))
print(q)