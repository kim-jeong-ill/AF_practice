#방학 숙제

"""
f = [] #0 -> 방학 일수, 1->수학, 2->국어, 3->국어가능, 4->수학가능

for _ in range(5):
    a = int(input())
    f.append(a)

f[0] = f[0] - (f[1] // f[4] + 1)
f[0] = f[0] - (f[2] // f[3] + 1)

print(f_l[0])
"""

l = int(input())
m = int(input())
k = int(input())
kp = int(input())
mp = int(input())

if m % mp == 0:
    l = l - (m // mp)
else:
    l = l - (m // mp) + 1
if k % kp == 0:
    l = l - (k // kp)
else:
    l = l - (k // kp) + 1

print(l)