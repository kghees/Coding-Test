n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
d = [[0]*i for i in range(1, n+1)]
d[0][0] = a[0][0]
for i in range(1, n):
  for j in range(i+1):
    if j == 0:
      d[i][j] = d[i-1][j] + a[i][j]
    elif i == j:
      d[i][j] = d[i-1][j-1] + a[i][j]
    else:
      d[i][j] = max(d[i-1][j-1], d[i-1][j]) + a[i][j]
print(max(d[n-1]))