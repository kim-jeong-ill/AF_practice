#스타후르츠

n, t, c, p = map(int, input().split()) # n : 여름 일수, t : 자라는 데 걸리는 일수,  c : 칸 수, p : 개 당 가격
n = n-1
x = n // t

print(x * c * p)