import sys
sys.setrecursionlimit(100000)
def dfs(x):
  check[x] = True
  for i in range(1, n+1):
    if not check[i] and a[x][i]:
      dfs(i)
n,m = map(int,input().split())
a = [[False]*(n+1) for _ in range(n+1)]
for _ in range(m):
  u,v = map(int,input().split())
  a[u][v] = True
  a[v][u] = True
check = [False]*(n+1)
cnt = 0
for i in range(1, n+1):
  if check[i] == False:
    dfs(i)
    cnt += 1
print(cnt)