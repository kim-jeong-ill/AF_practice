#단어 공부

s = str(input())
s = s.upper()

slist = list(set(s)) #set으로 중복 제거한 list만듬
cnt = []

for i in slist: # M I S P 4개만 검사
    count = s.count(i) #
    cnt.append(count)
    
print(cnt)
if cnt.count(max(cnt)) >=2:
    print('?')
else:
    print(slist[(cnt.index(max(cnt)))]) #cnt와 slist 단어의 순서가 같음