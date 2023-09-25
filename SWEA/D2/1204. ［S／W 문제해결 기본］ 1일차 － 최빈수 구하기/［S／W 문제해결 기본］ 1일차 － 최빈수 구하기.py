t = int(input())
for k in range(t):
  n = int(input())
  a = list(map(int,input().split()))
  d = [0]*1001
  for i in a:
    d[i] += 1
  result = 0
  cnt = 0
  for i in range(len(d)):
    if d[i] >= result:
      result = d[i]
      cnt = i
  print(f'#{k+1} {cnt}')