for t in range(10):
  n = int(input())
  code = [list(input()) for _ in range(8)]
  cnt = 0
  for i in range(8):
    for j in range(8-n+1):
      num = code[i][j:j+n]
      if num == num[::-1]:
        cnt += 1
  for i in range(8):
    for j in range(8-n+1):
      ans = ''
      for k in range(n):
        ans += code[j+k][i]
      if ans == ans[::-1]:
        cnt += 1
  print(f'#{t+1} {cnt}')