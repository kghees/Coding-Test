for t in range(1,11):
  n = int(input())
  a = list(map(int,input().split()))
  res = 0
  for i in range(2, len(a)-1):
    check = False
    for k in [-2,-1,1,2]:
      if a[i] > a[i+k]:
        check = True
      else:
        check = False
        break
    if check:
      ans = max(a[i-2],a[i-1],a[i+1],a[i+2])
      res += a[i] - ans
  print(f'#{t} {res}')