def dfs(x,cnt):
  global res
  res = max(res,cnt)
  for i in a[x]:
    if not check[i]:
      check[i] = True
      dfs(i,cnt+1)
      check[i] = False
for t in range(int(input())):
  n,m = map(int,input().split())
  a = [[] for _ in range(n+1)]
  for _ in range(m):
    u,v = map(int,input().split())
    a[u].append(v)
    a[v].append(u)
  res = 1
  for i in range(1, n+1):
    check = [False]*(n+1)
    check[i] = True
    dfs(i,1)
  print(f'#{t+1} {res}')