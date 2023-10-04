for t in range(int(input())):
  n = input()
  x = '0'
  cnt = 0
  for i in n:
    if x != i:
      x = i
      cnt += 1
  print(f'#{t+1} {cnt}')