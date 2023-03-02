#콘테스트

l1 = []
l2 = []

for _ in range(10):
    a = int(input())
    l1.append(a)
    
for _ in range(10):
    a = int(input())
    l2.append(a)
    
l1.sort()
l2.sort()
l1.reverse()
l2.reverse()

s1 = l1[0] + l1[1] + l1[2]
s2 = l2[0] + l2[1] + l2[2]

print(s1, s2)