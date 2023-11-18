from collections import deque
def bfs(x):
  q = deque()
  q.append(x)
  check[x] = True
  num[x] = 1
  while q:
    x = q.popleft()
    for i in d[x]:
      if not check[i]:
        check[i] = True
        num[i] = num[x]+1
        q.append(i)
for t in range(10):
  n, m = map(int,input().split())
  a = list(map(int,input().split()))
  d = [[] for _ in range(101)]
  for i in range(0,len(a),2):
    d[a[i]].append(a[i+1])
  check = [False]*101
  num = [0]*101
  bfs(m)
  res = 0
  k = 0
  for i in range(101):
    if k <= num[i]:
      k = num[i]
      res = i
  print(f'#{t+1} {res}')