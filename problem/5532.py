#방학 숙제

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

day1 = a // c
if a%c != 0:
    day1 += 1
day2 = b // d
if b%d != 0:
    day2 += 1

if day1 >= day2:
    print(l - day1)
else:
    print(l - day2)