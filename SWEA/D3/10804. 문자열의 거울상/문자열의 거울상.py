for t in range(int(input())):
  s = input()
  res = []
  for i in s:
    if i == 'b':
      res.append('d')
    elif i == 'p':
      res.append('q')
    elif i == 'q':
      res.append('p')
    elif i == 'd':
      res.append('b')
  res = res[::-1]
  print(f'#{t+1}',''.join(res))