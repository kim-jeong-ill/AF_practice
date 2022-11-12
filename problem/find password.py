#비밀번호 찾기 

m, n = map(int, input().split())

list1 = {}

for _ in range(m):
    domain, password = input().split()
    list1[domain] = password
    
for _ in range(n):
    print(list1[input().rstrip()])