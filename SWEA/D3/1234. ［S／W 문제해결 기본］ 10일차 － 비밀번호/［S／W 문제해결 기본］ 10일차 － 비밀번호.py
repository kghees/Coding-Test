for t in range(1, 11):
  n, s = input().split()
  n = int(n)
  s = list(s)
  i = 0
  while True:
    if s[i] == s[i+1]:
      del s[i:i+2]
      i -= 2
      n -= 2
    i += 1
    if i == n-1:
      break
  print(f'#{t}',end=' ')
  for i in s:
    print(i,end='')
  print()
      