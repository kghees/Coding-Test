n = int(input())
health = [0] + list(map(int,input().split()))
happy = [0] + list(map(int,input().split()))
d = [[0]*101 for _ in range(n+1)]
for i in range(1,n+1):
  for j in range(1,101):
    if health[i] <= j:
      d[i][j] = max(d[i-1][j], d[i-1][j-health[i]] + happy[i])
    else:
      d[i][j] = d[i-1][j]
print(d[n][99])