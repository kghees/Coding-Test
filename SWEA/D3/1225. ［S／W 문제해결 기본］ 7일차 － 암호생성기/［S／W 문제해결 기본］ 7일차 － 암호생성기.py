for t in range(10):
  n = int(input())
  a = list(map(int,input().split()))
  i = 1
  while True:
    a[0] -= i
    a.append(a.pop(0))
    if a[-1] <= 0:
      a[-1] = 0
      break
    i += 1
    if i > 5:
      i = 1
  print(f'#{t+1}',*a)