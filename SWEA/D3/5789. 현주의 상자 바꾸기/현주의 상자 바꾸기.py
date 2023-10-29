for t in range(int(input())):
  n,q = map(int,input().split())
  d = [0]*n
  for i in range(q):
    l,r = map(int,input().split())
    for j in range(l-1,r):
      d[j] = i+1
  print(f'#{t+1}',*d)