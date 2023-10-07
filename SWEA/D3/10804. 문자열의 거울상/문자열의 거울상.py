for t in range(int(input())):
  s = input()
  s = s[::-1]
  ans = ''
  for i in s:
    if i == 'q':
      ans += 'p'
    elif i == 'p':
      ans += 'q'
    elif i == 'b':
      ans += 'd'
    elif i == 'd':
      ans += 'b'
  print(f'#{t+1} {ans}')