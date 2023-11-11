from collections import deque
def bfs(x):
  q = deque()
  q.append(x)
  check[x] = True
  while q:
    x = q.popleft()
    for i in a[x]:
      if not check[i]:
        check[i] = True
        q.append(i)
for t in range(int(input())):
  n,m = map(int,input().split())
  a = [[] for _ in range(n+1)]
  for _ in range(m):
    u,v = map(int,input().split())
    a[u].append(v)
    a[v].append(u)
  check = [False]*(n+1)
  cnt = 0
  for i in range(1, n+1):
    if not check[i]:
      cnt += 1
      bfs(i)
  print(f'#{t+1} {cnt}')