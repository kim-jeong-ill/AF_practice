#달팽이는 올라가고 싶다.
import math

a,b,v =map(int, input().split())

day = math.ceil((v-a)/(a-b)) + 1
    
print(day)


'''
처음에 while문으로 시간 초과가 됐음
그래서 day를 기준으로 한 번에 구하는 식을 짰음
(a-b) * day + a = v
(a-b)* day=(v-a)
day = (v-a)/(a-b)
이고 
소수점 이하의 숫자가 나오는 것을 하루로 계산해서 +1을 해줌
((v-a)/(a-b)) + 1
'''