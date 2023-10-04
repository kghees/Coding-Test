for t in range(1,11):
  n = int(input())
  a = [input() for _ in range(8)]
  cnt = 0
  for i in range(8):
    for j in range(8-n+1):
      if a[i][j:j+n] == a[i][j:j+n][::-1]:
        cnt += 1
      ans = ''
      for k in range(n):
        ans += a[j+k][i]
      if ans == ans[::-1]:
        cnt += 1
  print(f'#{t} {cnt}')