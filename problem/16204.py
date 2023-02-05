#카드 뽑기

n,m,k = map(int, input().split()) # m = O, k = X

print(min(m, k) + n - max(m, k))