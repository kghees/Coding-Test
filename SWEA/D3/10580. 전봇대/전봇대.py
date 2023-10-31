for t in range(int(input())):
  n = int(input())
  res = []
  cnt = 0
  for _ in range(n):
    a,b = map(int,input().split())
    if res:
      for x,y in res:
        if (x > a and y < b) or (x < a and y > b):
          cnt += 1
    res.append((a,b))
  print(f'#{t+1} {cnt}')