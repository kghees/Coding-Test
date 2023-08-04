for t in range(int(input())):
  arr = [list(map(str,input())) for _ in range(5)]
  s = [[0]*15 for _ in range(15)]
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      s[i][j] = arr[i][j]
  ans = ''
  for k in range(15):
    for l in range(15):
      if s[l][k] != 0:
        ans += s[l][k]
  print(f'#{t+1} {ans}')