#과목선택

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

l1 = [a,b,c,d]
l2 = [e,f]

l1.sort()
l1.reverse()
l2.sort()
l2.reverse()

result1 = l1[0] + l1[1] + l1[2]

result2 = l2[0]

print(result1 + result2)