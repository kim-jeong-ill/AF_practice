""""
# A+B-2

test = int(input())

test_n = test

li = []

while test > 0:
    A, B = input().split()
    A = int(A)
    B = int(B)
    li.append(A+B)
    test = test - 1

m = 0
while test_n > 0:
    print(li[m])
    test_n = test_n - 1
    m = m + 1
    
"""

"""
#A+B-4
try:
    while 1:
        A, B = map(int, input().split())
        print(A+B)
except:
    exit()
"""


"""
#A+B-5
while 1:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    print(A+B)
"""


"""
#A+B-6
test = int(input())

test_n = test

li = []

while test > 0:
    A, B = map(int, input().split(','))
    li.append(A+B)
    test -= 1
    
    
n = 0
while test_n > 0:
    print(li[n])
    n += 1
    test_n -= 1
"""


"""
#A+B-7
test = int(input())

test_n = test

li = []

while test > 0:
    A, B = map(int, input().split())
    li.append(A+B)
    test -= 1
    
    
n = 0
while test_n > 0:
    print("Case #{}:".format(n+1), li[n])
    n += 1
    test_n -= 1
"""

"""
#A+B-8
test = int(input())

test_n = test

li1 = []
li2 = []
result_li = []

while test > 0:
    A, B = map(int, input().split())
    li1.append(A)
    li2.append(B)
    result_li.append(A+B)
    test -= 1
    
    
n = 0
while test_n > 0:
    print("Case #{}:".format(n+1), li1[n], "+",li2[n],"=", result_li[n])
    n += 1
    test_n -= 1
    
"""

"""
#그대로 출력하기 1, 2 
while 1:
    try:
        print(input())
    except EOFError:
        break
"""

"""
#숫자의 합
input()
A = input()
list(A)
B = map(int, A)


sum = 0
for i in B:
    sum += i
    
print(sum)
"""

"""
sen = input()

for i in range(0, len(sen), 10):
    count = i + 10
    print(sen[i:i+10])
"""

"""
# 열 개씩 끊어 출력하기
sen = input()

n = 0 
while len(sen) > n:
    print(sen[n:n+10])
    n += 10
"""

"""
count = int(input())

num = 1

while num <= count:
    print(num)
    num += 1

"""

"""
#기찍 N
n = int(input())

num = n

while num > 0:
    print(num)
    num -= 1
"""

"""
#구구단
n = int(input())

m = 1

while m <= 9:
    print(n,"*",m,"=",n*m)
    m += 1
"""

"""
#2007년
x, y = map(int, input().split())

d = ["MON","TUE","WED","THU","FRI","SAT","SUN"]

sum_m = 0

x -= 1

while x>=1:
    if  x <= 7:
        if x%2 == 1:
            sum_m += 31
        else:
            if x==2:
                sum_m += 28
            else:
                sum_m += 30
    else:
        if x%2 == 0:
            sum_m += 31
        else:
            sum_m += 30
    x -= 1
    
sum = sum_m + y

print(d[sum%7-1])

"""

"""
#합
n = int(input())

sum = 0

while n>=1:
    sum += n
    n -= 1

print(sum)
"""


"""
#최소, 최대
n = int(input())

li = map(int, input().split())

li_l = list(li)

li_l.sort()
print(li_l[0], li_l[-1])
"""


"""
#별 찍기-1
n = int(input())

num = 1

while n >= num:
    print(num*"*")
    num += 1
"""


"""
#별 찍기 -2
n = int(input())

num = 1

while n > num:
    print(' ' * (n-num-1) , num * "*")
    num += 1
    
print(num * "*")

"""


"""
#별 찍기-3
n = int(input())

while n >= 1:
    print(n * '*')
    n -= 1
"""


"""
# 별 찍기 -4 
n = int(input())

num = n
while num >= 1:
    if num == n:
        print(num * "*")
    else:
    	print(' '*(n-num-1), num * "*")
    num -= 1
    
"""



"""
#별 찍기 - 5
n = int(input())

num_1 = 1

while num_1 < n:
    print(' '*(n-num_1-1),'*'*(2*num_1-1))
    num_1 += 1
    
print('*'*(2*n-1))
"""



"""
#별 찍기 - 8 
n = int(input())

num_1 = 1
num_2 = n-1

while num_1 < n:
    print('*'*num_1, ' '*((n-num_1)*2-2), '*'*num_1)
    num_1 += 1
    
print('*'*n*2)
    
while num_2 >= 1:
    print('*'*num_2, ' '*((n-num_2)*2-2),'*'*num_2)
    num_2 -= 1
    
"""


"""
#별 찍기 - 12
n = int(input())
num_1 = 1
num_2 = n - 1

while num_1< n:
    print(' '*(n-num_1-1), '*'*num_1)
    num_1 += 1
    
print('*'*n)
    
while num_2 >= 1:
    print(' '*(n-num_2-1), '*'*num_2)
    num_2 -= 1
"""


"""
#별 찍기 - 9
n = int(input())

if n == 1:
    print('*')

else:
    num_1 = 1
    num_2 = n

    print('*'*(2*num_2-1))

    while num_1 < n:
        print(' '*(num_1-1), '*'*(2*(num_2-1)-1))
        num_1 += 1
        num_2 -= 1
    
    num_3 = 1
    num_4 = n-1

    while num_3 < n-1:
        print(' '*(num_4-2),'*'*((num_3+1)*2-1))
        num_3 += 1
        num_4 -= 1
    
    print('*'*(2*n-1))
    
"""


"""
#별 찍기 - 16
n = int(input())

num = 1

while num <= n:
    print(' '*(n-1), end=' ')
    k = num
    while k > 0:
        if k%2 == 0:
            print('*', end=' ')
            k -= 1
        else:
            print(' ', end=' ')
            k -= 1
        print(' '*(n-1), end= ' ')
    num += 1
    
"""

"""
# 별 찍기 - 17
n = int(input())
num = 1
k = 0
while num <= n:
    print(' '*(n-1), end=' ')
    print('*', end = ' ')
    print(' '*(2*k-1))
    print('*',end=' ')
    print(' '*(n-1))
    k += 1
    num += 1
    
print('*'*(2*n-1))

"""

#17, 18 again

"""
#1로 만들기
n = int(input())

count = 0

while n > 1:
    if n%3 == 0:
        n = n/3
        count += 1
    if n%2 == 0:
        n = n/2
        count += 1
    else:
        n -= 1
        count += 1
        
print(count)

"""


"""
#타일링 런타임 에러
n = int(input())

count = 1
frist = 1
second = 1

while count < n:
    third = frist + second
    frist = second
    second = third
    count += 1
    
print(third)
"""



"""
#별 찍기 - 16
n = int(input())

num = 1

while num < n:
    k = 1
    print(' ' * (n- num), end = '')
    
    while k <= 2*num-1:
        if k%2 == 1:
            print('*', end = '')
            k += 1
        else:
            print(' ', end = '')
            k += 1
            
    print('\n', end = '')
    num += 1

x = 1
while x <= 2*n-1:
    if x%2 == 1:
        print('*', end = '')
    else:
        print(' ', end = '')
    x += 1
    
"""


"""
#별 찍기 - 17
n = int(input())

num = 1

while num < n:
    print(' '*(n-num-1),'*', end = '')
    if num == 1:
        print('\n', end='')
    else:
        print(' '*((num-1)*2-2), '*')
    num += 1
        
print('*'*(2*n-1))
"""

"""
#1로 만들기 - 틀림;;
n = int(input())

n1 = n
n2 = n

count_1 = 0

while 1 < n1:
    if (n1%3 == 0 and n1%2 == 0) or (n1%3==0 and n1%2 != 0):
        n1 = n1 / 3
        count_1 += 1
    else:
        n1 -= 1
        count_1 += 1

count_2 = 0

while 1 < n2:
    if (n2%3 == 0 and n2%2 == 0) or (n2%3==0 and n2%2 != 0):
        n2 = n2 / 3
        count_2 += 1
    elif n2%3 != 0 and n2%2 !=0:
        n2 -= 1
        count_2 += 1
    else:
        n2 = n2 / 2
        count_2 += 1

        

if count_1 > count_2:
    print(count_2)
else:
    print(count_1)
"""
