n = int(input())
ans = 1000*1000+1
a = [[0]*n for _ in range(n+1)]
for i in range(1,n+1):
  a[i][0], a[i][1], a[i][2] = map(int,input().split())
d = [[0]*n for _ in range(n+1)]
for k in range(3):
  for j in range(3):
    if j == k:
      d[1][j] = a[1][j]
    else:
      d[1][j] = ans
  for i in range(2, n+1):
    d[i][0] = min(d[i-1][1], d[i-1][2]) + a[i][0]
    d[i][1] = min(d[i-1][0], d[i-1][2]) + a[i][1]
    d[i][2] = min(d[i-1][0], d[i-1][1]) + a[i][2]
  for j in range(3):
    if j == k:
      continue
    else:
      ans = min(ans,d[n][j])
print(ans)