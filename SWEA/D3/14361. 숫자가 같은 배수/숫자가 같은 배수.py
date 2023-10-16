for t in range(int(input())):
  n = list(input())
  num = int(''.join(n))
  n.sort()
  check = False
  i = 2
  m = int(''.join(sorted(n, reverse=True)))
  while (i*num <= m):
    x = i*num
    y = str(x)
    arr = []
    for j in y:
      arr.append(j)
    arr.sort()
    if n == arr:
      check = True
      break
    i += 1
  if check:
    print(f'#{t+1} possible')
  else:
    print(f'#{t+1} impossible')