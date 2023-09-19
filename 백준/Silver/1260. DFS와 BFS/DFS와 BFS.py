from collections import deque
def dfs(x):
  global check
  check[x] = True
  print(x,end=' ')
  for i in a[x]:
    if check[i] == False:
      dfs(i)
def bfs(start):
  check = [False]*(n+1)
  q = deque()
  q.append(start)
  check[start] = True
  while q:
    x = q.popleft()
    print(x,end=' ')
    for i in a[x]:
      if check[i] == False:
        check[i] = True
        q.append(i)
n,m,start = map(int,input().split())
a = [[] for _ in range(n+1)]
check = [False]*(n+1)
for _ in range(m):
  u,v = map(int,input().split())
  a[u].append(v)
  a[v].append(u)
for i in range(1, n+1):
  a[i].sort()
dfs(start)
print()
bfs(start)
print()