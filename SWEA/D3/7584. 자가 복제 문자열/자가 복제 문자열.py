for t in range(int(input())):
  k = int(input())
  res = 0
  k -= 1
  while k >= 0:
    if k % 2 == 1:
      k = (k-1)//2
    if k % 4 == 0:
      res = 0
      break
    elif k % 2 == 0:
      res = 1
      break
  print(f'#{t+1} {res}')