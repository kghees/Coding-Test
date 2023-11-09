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
        num[i] = num[x] + 1
        q.append(i)
for t in range(1,11):
  n,start = map(int,input().split())
  a = list(map(int,input().split()))
  d = [[] for _ in range(101)]
  for i in range(0,n,2):
    d[a[i]].append(a[i+1])
  check = [False]*(101)
  num = [0]*(101)
  bfs(start)
  res = 0
  k = 0
  for i in range(1, 101):
    if k <= num[i]:
      k = num[i]
      res = i
  print(f'#{t} {res}')