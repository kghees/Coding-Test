def long(a,b):
  global cnt
  cnt = max(cnt,b)
  for k in range(1, n+1):
    if path[a][k] and not visited[k]:
      visited[k] = 1
      long(k,b+1)
      visited[k] = 0
for t in range(int(input())):
  n, m = map(int,input().split())
  path = [[0 for _ in range(n+1)] for _ in range(n+1)]
  cnt = 1
  for _ in range(m):
    x, y = map(int,input().split())
    path[x][y] = 1
    path[y][x] = 1
  for i in range(1, n+1):
    visited = [0]*(n+1)
    visited[i] = 1
    long(i,1)
  print(f'#{t+1} {cnt}')