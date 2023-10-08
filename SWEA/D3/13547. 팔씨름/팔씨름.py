for t in range(int(input())):
  s = input()
  cnt = 0
  for i in s:
    if i == 'x':
      cnt += 1
  if cnt < 8:
    print(f'#{t+1} YES')
  else:
    print(f'#{t+1} NO')