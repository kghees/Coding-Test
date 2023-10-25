for t in range(1,11):
  n = int(input())
  a = list(map(int,input().split()))
  i = 1
  while True:
    if a[-1] <= 0:
      a[-1] = 0
      break
    a[0] -= i
    i += 1
    a.append(a.pop(0))
    if i > 5:
      i = 1
  print(f'#{t}',*a)