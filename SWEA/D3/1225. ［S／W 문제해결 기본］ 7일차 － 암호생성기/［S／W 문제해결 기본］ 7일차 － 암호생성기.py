for t in range(1,11):
  n = int(input())
  a = list(map(int,input().split()))
  x = 1
  while True:
    a[0] -= x
    a.append(a.pop(0))
    x += 1
    if x > 5:
      x = 1
    if a[-1] <= 0:
      a[-1] = 0
      break
  print(f'#{t}',end=' ')
  print(*a)