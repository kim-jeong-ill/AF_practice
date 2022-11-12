#팩토리얼 0의 개수

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(3))