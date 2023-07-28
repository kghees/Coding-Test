def visited(x):
  for i in range(x):
    if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
      return False
  return True
def queen(x):
  global result
  if x == n:
    result += 1
  else:
    for i in range(n):
      row[x] = i
      if visited(x):
        queen(x+1)
for t in range(int(input())):
  n = int(input())
  row = [0]*n
  result = 0
  queen(0)
  print(f'#{t+1} {result}')