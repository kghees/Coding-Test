for t in range(int(input())):
  n = int(input())
  a = [list(map(int,input().split())) for _ in range(n)]
  a_90 =[[0]*n for _ in range(n)]
  a_180 = [[0]*n for _ in range(n)]
  a_270 = [[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      a_90[i][j] = a[n-j-1][i]
      a_180[i][j] = a[n-i-1][n-j-1]
      a_270[i][j] = a[j][n-i-1]
  print(f'#{t+1}')
  for i in range(n):
    for j in range(n):
      print(a_90[i][j],end='')
    print(end=' ')
    for k in range(n):
      print(a_180[i][k],end='')
    print(end=' ')
    for l in range(n):
      print(a_270[i][l],end='')
    print()