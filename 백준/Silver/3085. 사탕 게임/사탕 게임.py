def check(a):
  x = len(a)
  t = 1
  for i in range(x):
    cnt = 1
    for j in range(1, x):
      if a[i][j] == a[i][j-1]:
        cnt += 1
      else:
        cnt = 1
      if t < cnt:
        t = cnt
    cnt = 1
    for j in range(1, x):
      if a[j][i] == a[j-1][i]:
        cnt += 1
      else:
        cnt = 1
      if t < cnt:
        t = cnt
  return t
n = int(input())
a = [list(input()) for _ in range(n)]
ans = 0
for i in range(n):
  for j in range(n):
    if j+1 < n:
      a[i][j],a[i][j+1] = a[i][j+1],a[i][j]
      temp = check(a)
      if ans < temp:
        ans = temp
      a[i][j],a[i][j+1] = a[i][j+1],a[i][j]
    if i+1 < n:
      a[i][j],a[i+1][j] = a[i+1][j],a[i][j]
      temp = check(a)
      if ans < temp:
        ans = temp
      a[i][j],a[i+1][j] = a[i+1][j],a[i][j]
print(ans)