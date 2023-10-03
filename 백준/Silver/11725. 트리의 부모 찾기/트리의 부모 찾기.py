from collections import deque
n = int(input())
a = [[] for _ in range(n+1)]
for _ in range(n-1):
  u,v = map(int,input().split())
  a[u].append(v)
  a[v].append(u)
visited = [0]*(n+1)
def bfs(x):
  q = deque()
  q.append(x)
  while q:
    x = q.popleft()
    for i in a[x]:
      if visited[i] == 0:
        visited[i] = x
        q.append(i)
bfs(1)
for i in range(2, n+1):
  print(visited[i])