dx = [1,1,0,1]
dy = [0,-1,1,1]
def omok():
  for i in range(n):
    for j in range(n):
      if a[i][j] == 'o':
        for k in range(4):
          x,y = i,j
          cnt = 0
          while 0 <= x < n and 0 <= y < n and a[x][y] == 'o':
            cnt += 1
            x += dx[k]
            y += dy[k]
          if cnt >= 5:
            return 'YES'
  return 'NO'
for t in range(int(input())):
  n = int(input())
  a = [input() for _ in range(n)]
  print(f'#{t+1} {omok()}')