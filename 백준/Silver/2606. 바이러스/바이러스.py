def dfs(x):
  global cnt
  visited[x] = True
  for i in a[x]:
    if visited[i] == False:
      cnt += 1
      dfs(i)
t = int(input())
n = int(input())
a = [[] for _ in range(t+1)]
for _ in range(n):
  u,v = map(int,input().split())
  a[u].append(v)
  a[v].append(u)
visited = [False]*(t+1)
cnt = 0
dfs(1)
print(cnt)