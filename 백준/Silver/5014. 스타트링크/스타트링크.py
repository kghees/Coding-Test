from collections import deque
def bfs(x):
  q = deque()
  q.append(x)
  check[x] = True
  button[x] = 0
  while q:
    x = q.popleft()
    for nx in [x+u,x-d]:
      if 0 < nx <= f and not check[nx]:
        check[nx] = True
        button[nx] = button[x] + 1
        q.append(nx)
f,s,g,u,d = map(int,input().split())
check = [False]*(f+1)
button = [-1]*(f+1)
bfs(s)
if button[g] == -1:
  print('use the stairs')
else:
  print(button[g])