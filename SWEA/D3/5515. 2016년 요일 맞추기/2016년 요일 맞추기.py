month = [i for i in range(12)]
for i in range(1,13):
  if i == 2:
    month[i-1] = [0 for _ in range(29)]
  elif i in [4,6,9,11]:
    month[i-1] = [0 for _ in range(30)]
  else:
    month[i-1] = [0 for _ in range(31)]
day = 4
for i in range(12):
  for j in range(len(month[i])):
    month[i][j] = day % 7
    day += 1
for t in range(int(input())):
  m,d = map(int,input().split())
  print(f'#{t+1} {month[m-1][d-1]}')