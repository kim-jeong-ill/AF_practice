#전자레인지

a = int(input()) # 현재 온도
b = int(input()) # 목표 온도
c = int(input()) # 0도 미만일때 1도 올리는 데 필요한 시간
d = int(input()) # 0도 일때 걸리는 해동 시간
e = int(input()) # 0도 초과 일때 1도 올리는 데 필요한 시간

if a < 0:
    t = -a * c + d + b * e
else:
    t = (b-a) * e
    
print(t)