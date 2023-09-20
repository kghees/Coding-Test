import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
k = int(input())
for _ in range(k):
  n,m = map(int,input().split())
  a = [[] for _ in range(n+1)]
  color = [0]*(n+1)
  for _ in range(m):
    u,v = map(int,input().split())
    a[u].append(v)
    a[v].append(u)
  def dfs(x, c):
    color[x] = c
    for i in a[x]:
      if not color[i]:
        dfs(i,3-c)
  ans = True
  for i in range(n):
    if not color[i]:
      dfs(i,1)
  for i in range(n):
    for j in a[i]:
      if color[i] == color[j]:
        ans = False
  if ans:
    print('YES')
  else:
    print('NO')