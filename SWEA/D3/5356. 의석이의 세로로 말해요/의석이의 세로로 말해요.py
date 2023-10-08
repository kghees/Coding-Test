for t in range(int(input())):
  a = [input() for _ in range(5)]
  s = [[0]*15 for _ in range(5)]
  for i in range(len(a)):
    for j in range(len(a[i])):
      s[i][j] = a[i][j]
  ans = ''
  for i in range(len(s[i])):
    for j in range(len(s)):
      if s[j][i] != 0:
        ans += s[j][i]
  print(f'#{t+1} {ans}')