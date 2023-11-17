for t in range(int(input())):
  n = int(input())
  a = [list(input()) for _ in range(n)]
  res = 0
  x,y = n//2,n//2
  for i in range(n):
    for j in range(x,y+1):
      res += int(a[i][j])
    if n//2 > i:
      x -= 1
      y += 1
    else:
      x += 1
      y -= 1
  print(f'#{t+1} {res}')