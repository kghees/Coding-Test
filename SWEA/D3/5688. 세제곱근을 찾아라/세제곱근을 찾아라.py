for t in range(int(input())):
  n = int(input())
  x = int(round(n**(1/3)))
  if x**3 == n:
    print(f'#{t+1} {x}')
  else:
    print(f'#{t+1} -1')