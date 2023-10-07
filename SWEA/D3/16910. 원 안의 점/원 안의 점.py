for t in range(int(input())):
  n = int(input())
  x = [i for i in range(-n, n+1)]
  y = [i for i in range(-n, n+1)]
  cnt = 0
  for i in range(len(x)):
    for j in range(len(y)):
      if (x[i]**2) + (y[j]**2) <= n**2:
        cnt += 1
  print(f'#{t+1} {cnt}')