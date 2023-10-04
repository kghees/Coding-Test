for t in range(int(input())):
  a,b = map(int,input().split())
  cnt = 0
  for i in range(a, b+1):
    x = i**(1/2)
    if x == int(x):
      i = str(i)
      x = str(int(x))
      if i == i[::-1] and x == x[::-1]:
        cnt += 1
  print(f'#{t+1} {cnt}')