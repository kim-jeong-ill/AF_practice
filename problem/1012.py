#유기농 배추

t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = [(x, y)]
    matrix[x][y] = 0
    
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
                
            if matrix[nx][ny] == 1:
                queue.append((nx, ny))
                matrix[nx][ny] = 0

for _ in range(t):
    m, n, k = map(int, input().split())
    matrix = [[0]*n for _ in range(m)]

    for _ in range(k):
        a, b = map(int, input().split())
        matrix[a][b] = 1
        
    cnt = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                bfs(i,j)
                cnt += 1
                
    print(cnt)