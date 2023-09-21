t = int(input())
d = [[0]*101 for _ in range(101)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(t):
  x,y = map(int,input().split())
  for i in range(10):
    for j in range(10):
      d[x+i][y+j] = 1
  result = 0
  for i in range(101):
    for j in range(101):
      for k in range(4):
        if d[i][j] == 1 and d[i+dx[k]][j+dy[k]] == 0:
          result += 1
print(result)