#짝수를 찾아라

T = int(input())

for _ in range(T):
    test_set = map(int, input().split())
    
    new_set = []
    
    for i in test_set:
        if i % 2 == 0:
            new_set.append(i)
    
    new_set.sort()
    sum1 = 0
    
    for j in new_set:
        sum1 += j
        
    print(sum1, new_set[0])