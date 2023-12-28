for t in range(int(input())):
  n = int(input())
  a = list(map(int,input().split()))
  d = [0]*1001
  for i in a:
    d[i] += 1
  res = 0
  cnt = 0
  for i in range(len(d)):
    if d[i] >= res:
      res = d[i]
      cnt = i
  print(f'#{t+1} {cnt}')