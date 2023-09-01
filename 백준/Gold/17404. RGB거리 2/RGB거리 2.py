n = int(input())
a = [[0,0,0]] + [list(map(int,input().split())) for _ in range(n)]
d = [[0]*3 for _ in range(n+1)]
ans = 1000*1000+1
for i in range(3):
  for j in range(3):
    if i == j:
      d[1][j] = a[1][j]
    else:
      d[1][j] = ans
  for k in range(2, n+1):
    d[k][0] = min(d[k-1][1], d[k-1][2]) + a[k][0]
    d[k][1] = min(d[k-1][0], d[k-1][2]) + a[k][1]
    d[k][2] = min(d[k-1][0],d[k-1][1]) + a[k][2]
  for l in range(3):
    if i == l:
      continue
    ans = min(ans, d[n][l])
print(ans)