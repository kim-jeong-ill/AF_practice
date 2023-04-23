#셀프 넘버

num = set(range(1,10001))
remove_list = set()
for i in num:
    for j in str(i):
        i += int(j)
    remove_list.add(i)
    
self_num = sorted(num - remove_list)
for k in self_num:
    print(k)