for t in range(int(input())):
  n = int(input())
  d = [[0]*i for i in range(1,n+1)]
  d[0][0] = 1
  for i in range(1,n):
    for j in range(i+1):
      if i == j or j == 0:
        d[i][j] = 1
      else:
        d[i][j] = d[i-1][j-1] + d[i-1][j]
  print(f'#{t+1}')
  for i in d:
    print(*i)