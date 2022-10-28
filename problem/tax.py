#세금

n = int(input())

first = int(n/100*78)
second = int(n/100*80 + (n/100*20)/100*78)

print(first, second)