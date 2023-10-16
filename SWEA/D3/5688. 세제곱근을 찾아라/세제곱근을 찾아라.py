for t in range(int(input())):
  n = int(input())
  result = round(pow(n,1/3))
  if result ** 3 == n:
    print(f'#{t+1} {result}')
  else:
    print(f'#{t+1} -1')