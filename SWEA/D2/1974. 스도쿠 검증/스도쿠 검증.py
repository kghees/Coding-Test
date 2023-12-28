def check(a):
  for i in range(9):
    row = [0]*10
    col = [0]*10
    for j in range(9):
      row[a[i][j]] += 1
      if row[a[i][j]] >= 2:
        return 0
      col[a[j][i]] += 1
      if col[a[j][i]] >= 2:
        return 0
    for k in range(0,9,3):
      for l in range(0,9,3):
        square = [0]*10
        for x in range(3):
          for y in range(3):
            square[a[k+x][l+y]] += 1
            if square[a[k+x][l+y]] >= 2:
              return 0
  return 1
for t in range(int(input())):
  a = [list(map(int,input().split())) for _ in range(9)]
  print(f'#{t+1} {check(a)}')