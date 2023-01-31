#n-queen
#다시 풀자;;

n = int(input())
count = 0
rows = [0] * n

# 현재 놓은 퀸 자리가 유효한지 체크
def check(r):
    for i in range(r):
        # 세로 체크
        if rows[i] == rows[r]:
            return False
        # 대각선 체크
        if abs(r - i) == abs(rows[r] - rows[i]):
            return False
    return True

# r행에 퀸을 놓아보기
def put_queen(r):
    global count
    if r == n:
        count += 1
        return
    
    for i in range(n):
        rows[r] = i
        if check(r):
            # 해당 자리에 놓을 수 있다면 다음행으로!
            put_queen(r + 1)
    
put_queen(0)
print(count)