for t in range(int(input())):
  n = int(input())
  a = [list(input()) for _ in range(n)]
  x,y = n//2,n//2
  res = 0
  for i in range(n):
    for j in range(x,y+1):
      res += int(a[i][j])
    if i < n//2:
      x -= 1
      y += 1
    else:
      x += 1
      y -= 1
  print(f'#{t+1} {res}')