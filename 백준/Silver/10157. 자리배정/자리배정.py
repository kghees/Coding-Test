c,r = map(int,input().split())
k = int(input())
seat = [[0]*c for _ in range(r)]
if c*r < k:
  print(0)
  exit()
dx = [0,1,0,-1]
dy = [-1,0,1,0]
d,x,y, = 0,0,0
for i in range(1, c*r+1):
  if i == k:
    print(y+1,x+1)
    break
  else:
    seat[x][y] = i
    x += dx[d]
    y += dy[d]
    if x < 0 or y < 0 or x >= r or y >= c or seat[x][y]:
      x -= dx[d]
      y -= dy[d]
      d = (d+1) % 4
      x += dx[d]
      y += dy[d]