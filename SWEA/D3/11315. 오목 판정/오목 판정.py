def omok():
  dx = [0,1,1,1]
  dy = [1,0,1,-1]
  for i in range(n):
    for j in range(n):
      if s[i][j] == 'o':
        for k in range(4):
          x = i
          y = j
          cnt = 0
          while 0 <= x < n and 0 <= y < n and s[x][y] == 'o':
            cnt += 1
            x += dx[k]
            y += dy[k]
          if cnt >= 5:
            return 'YES'
  return 'NO'
          
for t in range(int(input())):
  n = int(input())
  s = [input() for _ in range(n)]
  print(f'#{t+1} {omok()}')