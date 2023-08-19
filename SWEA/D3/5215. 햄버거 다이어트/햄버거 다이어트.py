for t in range(int(input())):
  n, l = map(int,input().split())
  arr = [[0,0]]
  for _ in range(n):
    arr.append(list(map(int,input().split())))
  d = [[0 for _ in range(l+1)] for _ in range(n+1)]
  for i in range(1, n+1):
    for j in range(1, l+1):
      score = arr[i][0]
      cal = arr[i][1]
      if j < cal:
        d[i][j] = d[i-1][j]
      else:
        d[i][j] = max(d[i-1][j-cal] + score, d[i-1][j])
  print(f'#{t+1} {d[n][l]}')