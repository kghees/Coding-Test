import sys
sys.setrecursionlimit(100000)
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
  def dfs(x,c):
    color[x] = c
    for i in a[x]:
      if color[i] == 0:
        if not dfs(i,3-c):
          return False
      elif color[i] == color[x]:
        return False
    return True
  ans = True
  for i in range(1,n+1):
    if color[i] == 0:
      if not dfs(i,1):
        ans = False
  if ans:
    print('YES')
  else:
    print('NO')