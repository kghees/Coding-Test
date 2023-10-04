for t in range(int(input())):
  s = input()
  a,b = 1,1
  for i in s:
    if i == 'L':
      b += a
    elif i == 'R':
      a += b
  print(f'#{t+1} {a} {b}')