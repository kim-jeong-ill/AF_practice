#대표값2

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

avg = (n1+n2+n3+n4+n5) // 5
l = [n1,n2,n3,n4,n5]
l.sort()

print(avg)
print(l[2])