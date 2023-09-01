n, k = map(int,input().split())
arr = [[0,0]]
for _ in range(n):
  arr.append(list(map(int,input().split())))
d = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(1, n+1):
  for j in range(1, k+1):
    weight = arr[i][0]
    value = arr[i][1]
    if j < weight:
      d[i][j] = d[i-1][j]
    else:
      d[i][j] = max(d[i-1][j] ,d[i-1][j-weight]+value)
print(d[n][k])