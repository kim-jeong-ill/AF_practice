#대지

n = int(input())

l1 = []
l2 = []
for _ in range(n):
    a,b = map(int, input().split())
    l1.append(a)
    l2.append(b)
    
l1.sort()
l2.sort()

print((l1[-1]-l1[0])*(l2[-1]-l2[0]))