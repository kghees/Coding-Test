for t in range(int(input())):
  arr = [list(map(int,input().split())) for _ in range(9)]
  s = []
  for i in range(9):
    cnt = [0]*10
    for k in range(9):
      cnt[arr[i][k]] += 1
    s.append(cnt)
  for j in range(9):
    cnt = [0]*10
    for k in range(9):
      cnt[arr[k][j]] += 1
    s.append(cnt)
  for x in range(0,9,3):
    for y in range(0,9,3):
      cnt = [0]*10
      for a in range(3):
        for b in range(3):
          cnt[arr[x+a][y+b]] += 1
      s.append(cnt)
  result = 1
  for c in range(27):
    for d in range(1, 10):
      if s[c][d] != 1:
        result = 0
  print(f'#{t+1} {result}')