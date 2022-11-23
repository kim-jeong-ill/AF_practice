#나이순 정렬

n = int(input())
n_list = []
for i in range(n):
  num, name = map(str, input().split())
  num = int(num)
  n_list.append((num, name))

n_list.sort(key = lambda x : x[0])

for i in n_list:
  print(i[0], i[1])