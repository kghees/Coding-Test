for t in range(int(input())):
  a = [list(map(int,input().split())) for _ in range(9)]
  res = 1
  for i in range(9):
    num = [0]*(10)
    num1 = [0]*(10)
    for j in range(9):
      num[a[i][j]] += 1
      num1[a[j][i]] += 1
    if num[1:].count(1) != 9:
      res = 0
      break
    if num1[1:].count(1) != 9:
      res = 0
      break
  for i in range(0,9,3):
    for j in range(0,9,3):
      num2 = [0]*10
      for k in range(3):
        for l in range(3):
          num2[a[i+k][j+l]] += 1
      if num2[1:].count(1) != 9:
        res = 0
        break
    if not res:
      break
  print(f'#{t+1} {res}')