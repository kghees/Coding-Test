for t in range(int(input())):
  n = input()
  check = False
  num = n
  i = 2
  while True:
    num = list(str(int(n)*i))
    i += 1
    if len(n) != len(num):
      break
    if set(n) == set(num):
      check = True
      break
  if check:
    print(f'#{t+1} possible')
  else:
    print(f'#{t+1} impossible')