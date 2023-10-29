for t in range(int(input())):
  a = list(map(int,input().split()))
  res = []
  for i in range(len(a)):
    for j in range(i+1,len(a)):
      for k in range(j+1,len(a)):
        x = a[i]+a[j]+a[k]
        if x not in res:
          res.append(x)
  res.sort(reverse=True)
  print(f'#{t+1} {res[4]}')