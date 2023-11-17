for t in range(int(input())):
  n,m = map(int,input().split())
  r = [int(input()) for _ in range(n)]
  w = [int(input()) for _ in range(m)]
  park = [0]*n
  wait = []
  res = 0
  for i in range(2*m):
    x = int(input())
    if x < 0:
      index = park.index(abs(x))
      if wait:
        park[index] = wait.pop(0)
        res += r[index] * w[park[index]-1]
      else:
        park[index] = 0
    else:
      if 0 in park:
        index = park.index(0)
        park[index] = x
        res += r[index]*w[x-1]
      else:
        wait.append(x)
  print(f'#{t+1} {res}')