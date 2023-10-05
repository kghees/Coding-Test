for t in range(int(input())):
  n = int(input())
  a = [list(map(int,input())) for _ in range(n)]
  result = 0
  x,y = n//2, n//2
  for i in range(n):
    for j in range(x,y+1):
      result += a[i][j]
    if i < n//2:
      x -=1
      y += 1
    else:
      x += 1
      y -= 1
  print(f'#{t+1} {result}')