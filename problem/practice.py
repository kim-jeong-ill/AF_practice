'''
def counter():
    i = 0
    def count():
        nonlocal i
        i += 1
        return i
    return count
'''

x = input()
x.split(' ')
sen = x[0]
num = int(x[1])

print(sen)
print(num)