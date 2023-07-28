for t in range(int(input())):
  b = input()
  a = '0'
  cnt = 0
  for i in range(len(b)):
    if b[i] != a:
      a = b[i]
      cnt += 1
  print(f'#{t+1} {cnt}')