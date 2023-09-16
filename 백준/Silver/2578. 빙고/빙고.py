def bingo():
  num = 0
  for x in b:
    if x.count(0) == 5:
      num += 1
  for i in range(5):
    y = 0
    for j in range(5):
      if b[j][i] == 0:
        y += 1
    if y == 5:
      num += 1
  t1 = 0
  for i in range(5):
    if b[i][i] == 0:
      t1 += 1
  if t1 == 5:
    num += 1
  t2 = 0
  for i in range(5):
    if b[i][4-i] == 0:
      t2 += 1
  if t2 == 5:
    num += 1
  return num
b = [list(map(int,input().split())) for _ in range(5)]
c = []
for _ in range(5):
  c += list(map(int,input().split()))
cnt = 0
for i in range(25):
  for j in range(5):
    for k in range(5):
      if c[i] == b[j][k]:
        b[j][k] = 0
        cnt += 1
  if cnt >= 12:
    result = bingo()
    if result >= 3:
      print(i+1)
      break