for t in range(int(input())):
  n = int(input())
  bus = [0]*5001
  for _ in range(n):
    a,b = map(int,input().split())
    for i in range(a, b+1):
      bus[i] += 1
  p = int(input())
  res = []
  for i in range(p):
    c = int(input())
    res.append(bus[c])
  print(f'#{t+1}',*res)