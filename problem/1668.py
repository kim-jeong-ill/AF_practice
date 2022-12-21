#트로피 진열

n = int(input())
l = [int(input()) for _ in range(n)]
left_cnt = right_cnt = 0
left_max = right_max = 0
for i in l:
    if i > left_max:
        left_max = i
        left_cnt += 1
for i in l[::-1]:
    if i > right_max:
        right_max = i
        right_cnt += 1
print(left_cnt)
print(right_cnt)