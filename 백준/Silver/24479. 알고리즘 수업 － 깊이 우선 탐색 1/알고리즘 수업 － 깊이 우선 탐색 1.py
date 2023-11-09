import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def dfs(x):
  global cnt
  check[x] = cnt
  for i in a[x]:
    if not check[i]:
      cnt += 1
      dfs(i)
n,m,r = map(int,input().split())
a = [[] for _ in range(n+1)]
for _ in range(m):
  u,v = map(int,input().split())
  a[u].append(v)
  a[v].append(u)
check = [0]*(n+1)
cnt = 1
for i in range(n+1):
  a[i].sort()
dfs(r)
for i in range(1,n+1):
  print(check[i])