for t in range(int(input())):
  a,b = map(int,input().split())
  arr = list(map(int,input().split()))
  brr = list(map(int,input().split()))
  res = 0
  if a < b:
    for i in range(b-a+1):
      x = 0
      for j in range(a):
        x += arr[j]*brr[i+j]
      if res < x:
        res = x
  elif a > b:
    for i in range(a-b+1):
      x = 0
      for j in range(b):
        x += brr[j]*arr[i+j]
      if res < x:
        res = x
  else:
    for i in range(a):
      res += arr[i]*brr[i]
  print(f'#{t+1} {res}')