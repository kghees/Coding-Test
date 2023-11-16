for t in range(int(input())):
  n = int(input())
  res = 0
  x = 0
  for _ in range(n):
    a = list(map(int,input().split()))
    if a[0] == 1:
      x += a[1]
    elif a[0] == 2:
      if x - a[1] < 0:
        x = 0
      else:
        x -= a[1]
    res += x
  print(f'#{t+1} {res}')