dx = [0,0,-1,1]
dy = [-1,1,0,0]
def dfs(x,y,ans):
  global res
  ans += a[x][y]
  if len(ans) == 7:
    res.append(ans)
    return
  for k in range(4):
    nx = x + dx[k]
    ny = y + dy[k]
    if 0 <= nx < 4 and 0 <= ny < 4:
      dfs(nx,ny,ans)
for t in range(int(input())):
  a = [list(map(str,input().split())) for _ in range(4)]
  res = []
  for i in range(4):
    for j in range(4):
      dfs(i,j,'')
  res = set(res)
  print(f'#{t+1} {len(res)}')