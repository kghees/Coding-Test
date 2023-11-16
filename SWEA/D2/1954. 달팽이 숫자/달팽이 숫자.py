dx = [0,1,0,-1]
dy = [1,0,-1,0]
def dfs(idx,cnt,x,y):
  if cnt > n*n:
    return
  nx = x + dx[idx]
  ny = y + dy[idx]
  if 0 <= nx < n and 0 <= ny < n and a[nx][ny] == 0:
    a[nx][ny] = cnt
    dfs(idx,cnt+1,nx,ny)
  else:
    dfs((idx+1)%4,cnt,x,y)
for t in range(int(input())):
  n = int(input())
  a = [[0]*n for _ in range(n)]
  a[0][0] = 1
  dfs(0,2,0,0)
  print(f'#{t+1}')
  for i in range(n):
    for j in range(n):
      print(a[i][j],end=' ')
    print()