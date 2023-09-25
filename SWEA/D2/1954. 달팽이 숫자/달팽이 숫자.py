dx = [0,1,0,-1]
dy = [1,0,-1,0]
def dfs(idx,num,x,y):
  if num > n*n:
    return
  nx = x + dx[idx]
  ny = y + dy[idx]
  if 0 <= nx < n and 0 <= ny < n and d[nx][ny] == 0:
    d[nx][ny] = num
    dfs(idx,num+1,nx,ny)
  else:
    dfs((idx+1)%4,num,x,y)
for t in range(int(input())):
  n = int(input())
  d = [[0]*n for _ in range(n)]
  d[0][0] = 1
  dfs(0,2,0,0)
  print(f'#{t+1}')
  for i in range(n):
    for j in range(n):
      print(f'{d[i][j]}',end=' ')
    print()