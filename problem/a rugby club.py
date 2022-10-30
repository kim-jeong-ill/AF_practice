#럭비 클럽

while 1:
    n = input().split()
    name = n[0]
    age = int(n[1])
    weight = int(n[2])
    if name == '#' and age == 0 and weight == 0:
        break
    if age > 17 or weight >= 80:
        print(name, 'Senior')
    else:
        print(name, 'Junior')