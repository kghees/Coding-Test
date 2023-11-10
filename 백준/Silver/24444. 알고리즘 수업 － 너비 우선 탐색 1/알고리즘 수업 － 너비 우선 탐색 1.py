import sys
from collections import deque
input = sys.stdin.readline
def bfs(x):
  global cnt
  q = deque()
  q.append(x)
  check[x] = cnt
  while q:
    x = q.popleft()
    a[x].sort()
    for i in a[x]:
      if not check[i]:
        cnt += 1
        check[i] = cnt
        q.append(i)
n,m,r = map(int,input().split())
a = [[] for _ in range(n+1)]
for _ in range(m):
  u,v = map(int,input().split())
  a[u].append(v)
  a[v].append(u)
check = [0]*(n+1)
cnt = 1
bfs(r)
for i in range(1,n+1):
  print(check[i])