dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    a[x][y] = 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < 16 and 0 <= ny < 16:
            if a[nx][ny] == 0:
                dfs(nx, ny)
            elif a[nx][ny] == 3:
                a[nx][ny] = 1
                return

for t in range(1, 11):
    n = int(input())
    a = [list(map(int, input())) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if a[i][j] == 2:
                dfs(i, j)
    res = 1
    for i in range(16):
        for j in range(16):
            if a[i][j] == 3:
                res = 0
    print(f'#{t} {res}')
