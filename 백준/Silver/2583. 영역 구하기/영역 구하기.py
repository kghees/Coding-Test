import sys
sys.setrecursionlimit(11000)
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def dfs(x,y):
  global cnt
  if not (0 <= x < m and 0 <= y < n):
    return False
  if ans[x][y] == 0:
    ans[x][y] = 1
    cnt += 1
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      dfs(nx,ny)
    return True
  return False
m,n,k = map(int,input().split())
ans = [[0]*n for _ in range(m)]
for _ in range(k):
  a,b,c,d = map(int,input().split())
  for i in range(b,d):
    for j in range(a, c):
      ans[i][j] = 1
res = 0
cnt = 0
arr = []
for i in range(m):
  for j in range(n):
    if ans[i][j] == 0:
      if dfs(i,j):
        res += 1
        arr.append(cnt)
        cnt = 0
arr.sort()
print(res)
print(*arr)