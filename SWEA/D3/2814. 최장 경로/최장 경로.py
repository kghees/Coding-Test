def dfs1(v,cnt):
  global result
  result = max(cnt, result)
  for k in range(1, n+1):
    if path[v][k] and not visited[k]:
      visited[k] = 1
      dfs1(k,cnt+1)
      visited[k] = 0
for t in range(int(input())):
  n,m = map(int,input().split())
  path = [[0 for _ in range(n+1)] for _ in range(n+1)]
  for _ in range(m):
    x, y = map(int,input().split())
    path[x][y] = 1
    path[y][x] = 1

  result = 1
  for i in range(1, n+1):
    visited = [0]*(n+1)
    visited[i] = 1
    dfs1(i,1)
  print(f'#{t+1} {result}')