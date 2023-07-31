def dfs(a,cnt):
  global result
  visited[a] = 1
  for i in path[a]:
    if visited[i] == 0:
      dfs(i, cnt+1)
  visited[a] = 0 
  if result < cnt:
    result = cnt
for t in range(int(input())):
  n,m = map(int,input().split())
  path = [[] for _ in range(n+1)]
  visited = [0]*(n+1)
  for _ in range(m):
    x, y = map(int,input().split())
    path[x].append(y)
    path[y].append(x)
  cnt,result = 0, 0
  for i in range(1, n+1):
    dfs(i,1)
  print(f'#{t+1} {result}')