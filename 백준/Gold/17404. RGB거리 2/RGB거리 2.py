n = int(input())
rgb = [list(map(int,input().split())) for _ in range(n)]
ans = 1000*1000 + 1
for i in range(3):
  d = [[ans,ans,ans] for _ in range(n)]
  d[0][i] = rgb[0][i]
  for j in range(1, n):
    d[j][0] = min(d[j-1][1], d[j-1][2]) + rgb[j][0]
    d[j][1] = min(d[j-1][0],d[j-1][2]) + rgb[j][1]
    d[j][2] = min(d[j-1][0], d[j-1][1]) + rgb[j][2]
  for k in range(3):
    if i != k:
      ans = min(ans,d[-1][k])
print(ans)