for t in range(int(input())):
  a = [list(input()) for _ in range(5)]
  s = [[0]*15 for _ in range(5)]
  for i in range(5):
    for j in range(len(a[i])):
      s[i][j] = a[i][j]
  res = []
  for i in range(15):
    for j in range(5):
      if s[j][i] != 0:
        res.append(s[j][i])
  print(f'#{t+1}',''.join(res))