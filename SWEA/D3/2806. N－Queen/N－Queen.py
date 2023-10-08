def visit(x):
  for i in range(x):
    if check[x] == check[i] or abs(check[x]-check[i]) == x-i:
      return False
  return True
def dfs(x):
  global result
  if x == n:
    result += 1
  else:
    for i in range(n):
      check[x] = i
      if visit(x):
        dfs(x+1)
for t in range(int(input())):
  n = int(input())
  check = [0]*n
  result = 0
  dfs(0)
  print(f'#{t+1} {result}')