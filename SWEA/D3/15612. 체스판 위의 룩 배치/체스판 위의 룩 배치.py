def chess():
  row = [0,0,0,0,0,0,0,0]
  col = [0,0,0,0,0,0,0,0]
  cnt = 0
  for i in range(8):
    for j in range(8):
      if a[i][j] == 'O':
        row[i] += 1
        col[j] += 1
        cnt += 1
      if row[i] >= 2 or col[j] >= 2:
        return False
  if cnt == 8:
    return True
  else:
    return False
for t in range(int(input())):
  a = [input() for _ in range(8)]
  if chess():
    print(f'#{t+1} yes')
  else:
    print(f'#{t+1} no')