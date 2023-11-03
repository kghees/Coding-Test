def check(x):
  x = str(x)
  for i in range(len(x)-1):
    for j in range(i+1,len(x)):
      if int(x[i]) > int(x[j]):
        return False
  return True
for t in range(int(input())):
  n = int(input())
  a = list(map(int,input().split()))
  res = []
  for i in range(n-1):
    for j in range(i+1,n):
      x = a[i]*a[j]
      if check(x):
        res.append(x)
      else:
        continue
  if res:
    print(f'#{t+1} {max(res)}')
  else:
    print(f'#{t+1} -1')