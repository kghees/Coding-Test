for t in range(int(input())):
  n = input()
  cnt = 0
  x = '0'
  for i in n:
    if i != x:
      x = i
      cnt += 1
  print(f'#{t+1} {cnt}') 