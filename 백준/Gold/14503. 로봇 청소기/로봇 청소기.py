dx = [-1,0,1,0]
dy = [0,1,0,-1]
n,m = map(int,input().split())
r,c,d = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
check = [[False]*m for _ in range(n)]
check[r][c] = True
cnt = 1
while True:
  ans = 0
  for _ in range(4):
    d = (d+3)%4
    nx = r + dx[d]
    ny = c + dy[d]
    if 0 <= nx < n and 0 <= ny < m and not check[nx][ny]:
      if a[nx][ny] == 0:
        check[nx][ny] = True
        cnt += 1
        ans = 1
        r = nx
        c = ny
        break
  if ans == 0:
    if a[r-dx[d]][c-dy[d]] == 1:
      print(cnt)
      break
    else:
      r = r-dx[d]
      c = c-dy[d]