import sys
input = sys.stdin.readline
n, k = map(int,input().split())
d = [[1]*(n+1) for _ in range(n+1)]
for i in range(2, n+1):
  for j in range(1, i):
    d[i][j] = d[i-1][j-1] + d[i-1][j]
print(d[n][k] % 10007)