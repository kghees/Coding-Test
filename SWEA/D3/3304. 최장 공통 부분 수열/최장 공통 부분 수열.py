for t in range(int(input())):
  a, b = input().split()
  x,y = len(a),len(b)
  d = [[0]*(y+1) for _ in range(x+1)]
  for i in range(1, x+1):
    for j in range(1, y+1):
      if a[i-1] == b[j-1]:
        d[i][j] = d[i-1][j-1] + 1
      else:
        d[i][j] = max(d[i-1][j],d[i][j-1])
  print(f'#{t+1} {d[x][y]}')