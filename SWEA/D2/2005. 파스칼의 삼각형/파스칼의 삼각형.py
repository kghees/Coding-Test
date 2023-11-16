for t in range(int(input())):
  n = int(input())
  a = [[0]*i for i in range(1, n+1)]
  a[0][0] = 1
  for i in range(1,n):
    for j in range(len(a[i])):
      if j == 0:
        a[i][j] = a[i-1][j]
      elif i == j:
        a[i][j] = a[i-1][j-1]
      else:
        a[i][j] = a[i-1][j] + a[i-1][j-1]
  print(f'#{t+1}')
  for i in range(n):
    for j in range(len(a[i])):
      print(a[i][j],end=' ')
    print()