for t in range(int(input())):
  n = input()
  check = False
  x = n
  i = 2
  while True:
    x = str(int(n)*i)
    i += 1
    if len(n) != len(x):
      break
    if set(x) == set(n):
      check = True
      break
  if check:
    print(f'#{t+1} possible')
  else:
    print(f'#{t+1} impossible')