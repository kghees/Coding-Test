for t in range(int(input())):
  n,m = map(int,input().split())
  money = [int(input()) for _ in range(n)]
  weight = [int(input()) for _ in range(m)]
  park = [0]*n
  wait = []
  res = 0
  p = [int(input()) for _ in range(2*m)]
  for i in p:
    if i < 0:
      index = park.index(abs(i))
      if wait:
        a = wait.pop(0)
        park[index] = a
        res += money[index]*weight[a-1]
      else:
        park[index] = 0
    else:
      if 0 not in park:
        wait.append(i)
      else:
        index = park.index(0)
        park[index] = i
        res += money[index]*weight[i-1]
  print(f'#{t+1} {res}')