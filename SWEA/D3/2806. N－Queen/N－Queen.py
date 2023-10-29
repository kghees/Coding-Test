def check(x):
  for i in range(x):
    if d[x] == d[i] or abs(d[x]-d[i]) == x-i:
      return False
  return True
def dfs(x):
  global cnt
  if x == n:
    cnt += 1
  else:
    for i in range(n):
      d[x] = i
      if check(x):
        dfs(x+1)
for t in range(int(input())):
  n = int(input())
  d = [0]*n
  cnt = 0
  dfs(0)
  print(f'#{t+1} {cnt}')