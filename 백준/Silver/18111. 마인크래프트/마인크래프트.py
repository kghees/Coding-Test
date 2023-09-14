import sys
input = sys.stdin.readline
n,m,b = map(int,input().split())
e = [list(map(int,input().split())) for _ in range(n)]
floor = 0
ans = int(1e9)
for k in range(257):
  max_b,min_b = 0,0
  for i in range(n):
    for j in range(m):
      if e[i][j] >= k:
        max_b += e[i][j] - k
      else:
        min_b += k - e[i][j]
  if max_b + b >= min_b:
    if min_b + (max_b*2) <= ans:
      ans = min_b + (max_b*2)
      floor = k
print(ans,floor) 