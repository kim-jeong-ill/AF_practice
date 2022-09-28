#개수 세기

n = int(input())

n_list = input().split(' ') #1, 4, 1,2 ...
n_list = list(map(int, n_list))

f_number = int(input())

count = 0
for i in n_list:
    if f_number == i:
        count += 1
        
print(count)