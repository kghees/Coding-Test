n = 1000000
nlist = [True]*(n+1)
nlist[0], nlist[1] = False, False
for i in range(2,int(n**0.5)+1):
  if nlist[i]:
    for j in range(i*2,n+1,i):
      nlist[j] = False
for t in range(int(input())):
  d,a,b = map(int,input().split())
  cnt = 0
  for i in range(a, b+1):
    if nlist[i]:
      x = str(i)
      if str(d) in x:
        cnt += 1
  print(f'#{t+1} {cnt}')