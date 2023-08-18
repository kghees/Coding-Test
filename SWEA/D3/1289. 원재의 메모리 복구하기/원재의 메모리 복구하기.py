for t in range(int(input())):
  m = input()
  cnt = 0
  x = '0'
  for i in range(len(m)):
    if m[i] != x:
      x = m[i]
      cnt += 1
  print(f'#{t+1} {cnt}')