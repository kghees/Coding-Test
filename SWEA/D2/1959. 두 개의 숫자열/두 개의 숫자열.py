for t in range(int(input())):
  n,m = map(int,input().split())
  a = list(map(int,input().split()))
  b = list(map(int,input().split()))
  res = 0
  if len(a) > len(b):
    for i in range(len(a)-len(b)+1):
      x = 0
      for j in range(len(b)):
        x += a[i+j]*b[j]
      if res < x:
        res = x
  elif len(a) < len(b):
    for i in range(len(b)-len(a)+1):
      x = 0
      for j in range(len(a)):
        x += a[j]*b[i+j]
      if res < x:
        res = x
  else:
    for i in range(len(a)):
      res += a[i]*b[i]
  print(f'#{t+1} {res}') 