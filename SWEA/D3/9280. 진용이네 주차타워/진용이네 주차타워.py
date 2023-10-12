for t in range(int(input())):
  n, m = map(int,input().split())
  r = [int(input()) for _ in range(n)]
  w = [int(input()) for _ in range(m)]
  result = 0
  wait = []
  park = [0]*n
  s = [int(input()) for _ in range(2*m)]
  for i in s:
    if i < 0:
      k = park.index(abs(i))
      if wait:
        c = wait.pop(0)
        park[k] = c
        result += r[k]*w[c-1]
      else:
        park[k] = 0
    else:
      if 0 not in park:
        wait.append(i)
      else:
        k = park.index(0)
        park[k] = i
        result += r[k]*w[i-1]
  print(f'#{t+1} {result}')