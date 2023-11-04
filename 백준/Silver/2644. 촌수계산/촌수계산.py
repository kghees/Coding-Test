def dfs(x):
  check[x] = True
  for i in a[x]:
    if not check[i]:
      res[i] = res[x] + 1
      dfs(i)
n = int(input())
x,y = map(int,input().split())
m = int(input())
a = [[] for _ in range(n+1)]
for _ in range(m):
  u,v = map(int,input().split())
  a[u].append(v)
  a[v].append(u)
check = [False]*(n+1)
res = [0]*(n+1)
dfs(x)
if res[y] != 0:
  print(res[y])
else:
  print(-1)