t = int(input())
a = [[0]*101 for _ in range(101)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(t):
  x,y = map(int,input().split())
  for i in range(x,x+10):
    for j in range(y,y+10):
      a[i][j] = 1
result = 0
for i in range(1,101):
  for j in range(1,101):
    if a[i][j] == 1:
      cnt = 0
      for k in range(4):
        if a[i+dx[k]][j+dy[k]] == 1:
          cnt += 1
      if cnt == 3:
        result += 1
      elif cnt == 2:
        result += 2
print(result)