for t in range(int(input())):
  n = int(input())
  a = list(map(int,input().split()))
  a = a[::-1]
  res = 0
  x = 0
  for i in a:
    if x < i:
      x = i
    res += x - i
  if res > 0:
    print(f'#{t+1} {res}')
  else:
    print(f'#{t+1} 0')