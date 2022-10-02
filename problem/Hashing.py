#hint = 예제 1: abcde의 해시 값은 1 × 310 + 2 × 311 + 3 × 312 + 4 × 313 + 5 × 314 = 1 + 62 + 2883 + 119164 + 4617605 = 4739715이다.
'''
# 50점
L = int(input())
sentence = input()
sentence = list(sentence)
M = 1234567891
r = 31

Alphabet_dict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

sum = 0
for i in range(L):
    sum += Alphabet_dict[sentence[i]] * (31 ** i)
    
print(sum)
'''

L = int(input())
M = 1234567891
r = 31
sentence = input()
sum = 0

for i in range(L):
    num = ord(sentence[i]) - 96
    sum += num * (r ** i)
    
print(sum % M)