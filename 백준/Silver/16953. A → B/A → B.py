from collections import deque
def bfs(x,cnt):
  global res
  q = deque()
  q.append((x,cnt))
  while q:
    x,cnt = q.popleft()
    if x == b:
      res = cnt
      break
    for nx in [x*2,int(str(x)+'1')]:
      if nx <= b:
        q.append((nx,cnt+1))
a,b = map(int,input().split())
res = -1
bfs(a,1)
print(res)