from collections import deque
def bfs(x):
  q = deque()
  q.append(x)
  check[x] = True
  while q:
    x = q.popleft()
    for i in d[x]:
      if not check[i]:
        check[i] = True
        q.append(i)
for _ in range(int(input())):
  n = int(input())
  a = list(map(int,input().split()))
  d = [[] for _ in range(n+1)]
  for i in range(1, n+1):
    d[i].append(a[i-1])
    d[a[i-1]].append(i)
  check = [False]*(n+1)
  cnt = 0
  for i in range(1, n+1):
    if not check[i]:
      bfs(i)
      cnt += 1
  print(cnt)