import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
dx = [0,0,-1,1,-1,-1,1,1]
dy = [-1,1,0,0,1,-1,-1,1]
def dfs(x,y):
  if x < 0 or x >= h or y < 0 or y >= w:
    return False
  if d[x][y] == 1:
    d[x][y] = 0
    for k in range(8):
      nx = x + dx[k]
      ny = y + dy[k]
      dfs(nx,ny)
    return True
  return False
while True:
  w,h = map(int,input().split())
  if w == 0 and h == 0:
    break
  d = [list(map(int,input().split())) for _ in range(h)]
  result = 0
  for i in range(h):
    for j in range(w):
      if dfs(i,j):
        result += 1
  print(result)