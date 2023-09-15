n,m = map(int,input().split())
a = [input() for _ in range(n)]
t = min(n,m)
result = 0
for i in range(n):
  for j in range(m):
    for k in range(t):
      if i+k < n and j+k < m and a[i][j] == a[i][j+k] == a[i+k][j]== a[i+k][j+k]:
         result = max(result,(k+1)**2)
print(result)