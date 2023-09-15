n,m = map(int,input().split())
ice = [[False]*n for _ in range(n)]
result = 0
for _ in range(m):
  a, b = map(int,input().split())
  ice[a-1][b-1] = True
  ice[b-1][a-1] = True
for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      if not ice[i][j] and not ice[i][k] and not ice[j][k]:
        result += 1
print(result)